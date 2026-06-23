// TOON Converter Functions

function convertJsonToToon() {
    const input = document.getElementById('jsonInput').value;
    const toonOutput = document.getElementById('toonOutput');
    const treeView = document.getElementById('treeView');
    const alertsDiv = document.getElementById('alerts');

    alertsDiv.innerHTML = '';

    if (!input.trim()) {
        toonOutput.textContent = 'Aguardando conversão...';
        treeView.innerHTML = '<div class="tree-view">Aguardando conversão...</div>';
        updateStats(0, 0);
        return;
    }

    try {
        // Try to fix common JSON issues
        let fixedInput = input.trim();
        const singleQuotePattern = /'/g;
        fixedInput = fixedInput.replace(singleQuotePattern, '"');

        let jsonObj;
        try {
            jsonObj = JSON.parse(fixedInput);
        } catch (firstError) {
            try {
                jsonObj = JSON.parse(input);
            } catch (secondError) {
                throw new Error(`JSON inválido. Certifique-se de usar aspas duplas (") ao invés de aspas simples ('). Erro: ${firstError.message}`);
            }
        }

        const toonResult = jsonToToon(jsonObj);
        toonOutput.textContent = toonResult;

        // Render tree
        treeView.innerHTML = '';
        treeView.appendChild(createTreeElement(renderTree(jsonObj)));

        // Show success message if we had to fix the input
        if (fixedInput !== input) {
            showAlert('success', '✓ JSON corrigido automaticamente (aspas simples → duplas)');
        }

        // Update token statistics
        const jsonTokens = estimateTokens(JSON.stringify(jsonObj));
        const toonTokens = estimateTokens(toonResult);
        updateStats(jsonTokens, toonTokens);

    } catch (error) {
        toonOutput.textContent = 'Erro na conversão - verifique o JSON';
        treeView.innerHTML = '<div class="tree-view">Erro ao processar JSON</div>';
        showAlert('error', 'Erro: ' + error.message);
        updateStats(0, 0);
    }
}

function jsonToToon(obj, indent = 0) {
    let result = [];
    const spaces = '  '.repeat(indent);

    for (const [key, value] of Object.entries(obj)) {
        if (Array.isArray(value)) {
            if (value.length === 0) {
                result.push(`${spaces}${key}[0]:`);
            } else if (isUniformObjectArray(value)) {
                const fields = Object.keys(value[0]);
                result.push(`${spaces}${key}[${value.length}]{${fields.join(',')}}:`);
                value.forEach(item => {
                    const values = fields.map(field => formatValue(item[field]));
                    result.push(`${spaces}  ${values.join(',')}`);
                });
            } else if (isPrimitiveArray(value)) {
                const values = value.map(v => formatValue(v)).join(',');
                result.push(`${spaces}${key}[${value.length}]: ${values}`);
            } else {
                result.push(`${spaces}${key}[${value.length}]:`);
                value.forEach(item => {
                    if (typeof item === 'object' && item !== null && !Array.isArray(item)) {
                        const entries = Object.entries(item);
                        if (entries.length === 0) {
                            result.push(`${spaces}  -`);
                        } else {
                            const [firstKey, firstValue] = entries[0];

                            if (Array.isArray(firstValue)) {
                                if (isPrimitiveArray(firstValue)) {
                                    const vals = firstValue.map(v => formatValue(v)).join(',');
                                    result.push(`${spaces}  - ${firstKey}[${firstValue.length}]: ${vals}`);
                                } else {
                                    result.push(`${spaces}  - ${firstKey}[${firstValue.length}]:`);
                                    firstValue.forEach(arrItem => {
                                        if (typeof arrItem === 'object' && arrItem !== null && !Array.isArray(arrItem)) {
                                            const arrItemEntries = Object.entries(arrItem);
                                            if (arrItemEntries.length > 0) {
                                                const [afk, afv] = arrItemEntries[0];
                                                if (typeof afv === 'object' && afv !== null && !Array.isArray(afv)) {
                                                    result.push(`${spaces}    - ${afk}:`);
                                                    result.push(jsonToToon(afv, indent + 3));
                                                } else {
                                                    result.push(`${spaces}    - ${afk}: ${formatValue(afv)}`);
                                                }
                                                for (let j = 1; j < arrItemEntries.length; j++) {
                                                    const [ak, av] = arrItemEntries[j];
                                                    if (typeof av === 'object' && av !== null && !Array.isArray(av)) {
                                                        result.push(`${spaces}      ${ak}:`);
                                                        result.push(jsonToToon(av, indent + 4));
                                                    } else {
                                                        result.push(`${spaces}      ${ak}: ${formatValue(av)}`);
                                                    }
                                                }
                                            }
                                        } else {
                                            result.push(`${spaces}    ${formatValue(arrItem)}`);
                                        }
                                    });
                                }
                            } else if (typeof firstValue === 'object' && firstValue !== null) {
                                result.push(`${spaces}  - ${firstKey}:`);
                                result.push(jsonToToon(firstValue, indent + 3));
                            } else {
                                result.push(`${spaces}  - ${firstKey}: ${formatValue(firstValue)}`);
                            }

                            for (let i = 1; i < entries.length; i++) {
                                const [k, v] = entries[i];
                                if (Array.isArray(v)) {
                                    if (isPrimitiveArray(v)) {
                                        const vals = v.map(x => formatValue(x)).join(',');
                                        result.push(`${spaces}    ${k}[${v.length}]: ${vals}`);
                                    } else {
                                        result.push(`${spaces}    ${k}[${v.length}]:`);
                                        v.forEach(arrItem => {
                                            if (typeof arrItem === 'object' && arrItem !== null && !Array.isArray(arrItem)) {
                                                const arrItemEntries = Object.entries(arrItem);
                                                if (arrItemEntries.length > 0) {
                                                    const [afk, afv] = arrItemEntries[0];
                                                    if (typeof afv === 'object' && afv !== null && !Array.isArray(afv)) {
                                                        result.push(`${spaces}      - ${afk}:`);
                                                        result.push(jsonToToon(afv, indent + 4));
                                                    } else {
                                                        result.push(`${spaces}      - ${afk}: ${formatValue(afv)}`);
                                                    }
                                                    for (let j = 1; j < arrItemEntries.length; j++) {
                                                        const [ak, av] = arrItemEntries[j];
                                                        if (typeof av === 'object' && av !== null && !Array.isArray(av)) {
                                                            result.push(`${spaces}        ${ak}:`);
                                                            result.push(jsonToToon(av, indent + 5));
                                                        } else {
                                                            result.push(`${spaces}        ${ak}: ${formatValue(av)}`);
                                                        }
                                                    }
                                                }
                                            } else {
                                                result.push(`${spaces}      ${formatValue(arrItem)}`);
                                            }
                                        });
                                    }
                                } else if (typeof v === 'object' && v !== null) {
                                    result.push(`${spaces}    ${k}:`);
                                    result.push(jsonToToon(v, indent + 3));
                                } else {
                                    result.push(`${spaces}    ${k}: ${formatValue(v)}`);
                                }
                            }
                        }
                    } else if (Array.isArray(item)) {
                        const innerValues = item.map(v => formatValue(v)).join(',');
                        result.push(`${spaces}  - [${item.length}]: ${innerValues}`);
                    } else {
                        result.push(`${spaces}  - ${formatValue(item)}`);
                    }
                });
            }
        } else if (typeof value === 'object' && value !== null) {
            result.push(`${spaces}${key}:`);
            result.push(jsonToToon(value, indent + 1));
        } else {
            result.push(`${spaces}${key}: ${formatValue(value)}`);
        }
    }

    return result.join('\n');
}

function isUniformObjectArray(arr) {
    if (arr.length === 0) return false;
    if (typeof arr[0] !== 'object' || arr[0] === null || Array.isArray(arr[0])) {
        return false;
    }

    const firstKeys = Object.keys(arr[0]).sort();

    return arr.every(item => {
        if (typeof item !== 'object' || item === null || Array.isArray(item)) {
            return false;
        }

        const itemKeys = Object.keys(item).sort();
        if (itemKeys.length !== firstKeys.length) return false;
        if (!itemKeys.every((k, i) => k === firstKeys[i])) return false;

        return Object.values(item).every(v =>
            v === null ||
            typeof v === 'string' ||
            typeof v === 'number' ||
            typeof v === 'boolean'
        );
    });
}

function isPrimitiveArray(arr) {
    return arr.every(item =>
        item === null ||
        typeof item === 'string' ||
        typeof item === 'number' ||
        typeof item === 'boolean'
    );
}

function formatValue(value) {
    if (value === null) return 'null';
    if (typeof value === 'undefined') return 'null';
    if (typeof value === 'boolean') return value.toString();
    if (typeof value === 'number') {
        if (!isFinite(value)) return 'null';
        return value.toString();
    }
    if (typeof value === 'string') {
        return quoteStringIfNeeded(value);
    }
    return String(value);
}

function quoteStringIfNeeded(str) {
    if (str === '') return '""';
    if (str !== str.trim()) return `"${str}"`;
    if (str === 'true' || str === 'false' || str === 'null') return `"${str}"`;
    if (/^-?\d+(\.\d+)?$/.test(str)) return `"${str}"`;
    if (str.startsWith('- ')) return `"${str}"`;
    if (/[,:\\"']/.test(str)) return `"${escapeString(str)}"`;
    if (/^\[.*\]$/.test(str) || /^\{.*\}$/.test(str)) return `"${str}"`;
    return str;
}

function escapeString(str) {
    return str
        .replace(/\\/g, '\\\\')
        .replace(/"/g, '\\"')
        .replace(/\n/g, '\\n')
        .replace(/\r/g, '\\r')
        .replace(/\t/g, '\\t');
}

function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
}

// Tree rendering functions
function renderTree(data, key = null, isRoot = true) {
    const nodeClass = isRoot ? 'tree-node root' : 'tree-node';

    if (Array.isArray(data)) {
        const id = Math.random().toString(36).substr(2, 9);
        let html = `<div class="${nodeClass}">`;

        if (key) {
            html += `<div class="tree-item" onclick="toggleNode('${id}')">
                <span class="tree-toggle" id="toggle-${id}">▼</span>
                <span class="tree-key">${escapeHtml(key)}</span>
                <span class="tree-type"> [Array ${data.length} items]</span>
            </div>`;
        }

        html += `<div class="tree-children" id="children-${id}">`;

        data.forEach((item, index) => {
            html += renderTree(item, `[${index}]`, false);
        });

        html += '</div></div>';
        return html;
    }

    if (data && typeof data === 'object' && data !== null) {
        const id = Math.random().toString(36).substr(2, 9);
        let html = `<div class="${nodeClass}">`;

        if (key) {
            html += `<div class="tree-item" onclick="toggleNode('${id}')">
                <span class="tree-toggle" id="toggle-${id}">▼</span>
                <span class="tree-key">${escapeHtml(key)}</span>
                <span class="tree-type"> {Object}</span>
            </div>`;
        }

        html += `<div class="tree-children" id="children-${id}">`;

        for (const [k, v] of Object.entries(data)) {
            html += renderTree(v, k, false);
        }

        html += '</div></div>';
        return html;
    }

    let html = `<div class="${nodeClass}">`;
    html += `<div class="tree-item">`;
    html += `<span class="tree-toggle"></span>`;
    if (key) {
        html += `<span class="tree-key">${escapeHtml(key)}</span>: `;
    }
    html += `<span class="tree-value">${escapeHtml(formatTreeValue(data))}</span>`;
    html += `</div></div>`;

    return html;
}

function formatTreeValue(value) {
    if (value === null) return 'null';
    if (value === undefined) return 'undefined';
    if (typeof value === 'string') return `"${value}"`;
    if (typeof value === 'boolean') return value.toString();
    if (typeof value === 'number') return value.toString();
    return String(value);
}

function createTreeElement(html) {
    const wrapper = document.createElement('div');
    wrapper.innerHTML = html;
    return wrapper.firstChild;
}

function toggleNode(id) {
    const children = document.getElementById(`children-${id}`);
    const toggle = document.getElementById(`toggle-${id}`);

    if (children.classList.contains('collapsed')) {
        children.classList.remove('collapsed');
        toggle.textContent = '▼';
    } else {
        children.classList.add('collapsed');
        toggle.textContent = '▶';
    }
}
