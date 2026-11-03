// PEROVANO — comportamento do site. Tudo aqui é melhoria progressiva:
// sem JS o conteúdo, os links e a navegação continuam funcionando.
(function () {
  'use strict';

  var root = document.documentElement;
  root.classList.add('js');

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Textos de interface nos dois idiomas (a página define o idioma em <html lang>).
  var EN = /^en\b/i.test(root.lang);
  var T = EN ? {
    openMenu: 'Open menu',
    closeMenu: 'Close menu',
    cookieTitle: 'Analytics cookies',
    cookieText: 'We use Google Analytics to measure site traffic and understand which content is useful. ' +
      'These cookies are only enabled if you accept. <a href="/en/privacy.html#cookies">Privacy policy</a>',
    accept: 'Accept',
    decline: 'Decline',
    cookiePrefs: 'Cookie preferences',
    searchEmpty: function (q) { return 'No articles found for “' + q + '”. Try another term or pick a category.'; }
  } : {
    openMenu: 'Abrir menu',
    closeMenu: 'Fechar menu',
    cookieTitle: 'Cookies de medição',
    cookieText: 'Usamos o Google Analytics para medir a audiência do site e entender quais conteúdos são úteis. ' +
      'Esses cookies só são ativados se você aceitar. <a href="/privacy.html#cookies">Política de privacidade</a>',
    accept: 'Aceitar',
    decline: 'Recusar',
    cookiePrefs: 'Preferências de cookies',
    searchEmpty: function (q) { return 'Nenhum artigo encontrado para “' + q + '”. Tente outro termo ou escolha uma categoria.'; }
  };

  // Seletor PT/EN: a escolha manual vale mais que o idioma do navegador
  // (o redirecionamento automático fica no <head> da home em português).
  document.addEventListener('click', function (event) {
    var link = event.target.closest && event.target.closest('[data-lang]');
    if (!link) return;
    try { localStorage.setItem('perovano-lang', link.getAttribute('data-lang')); } catch (e) { /* segue pelo link */ }
  });

  // Âncoras do site anterior que podem ter links externos (só na versão em português).
  var legacyAnchors = EN ? {} : { '#servicos': '#solucoes', '#top': '#inicio' };
  var redirectLegacyAnchor = function () {
    if (legacyAnchors[location.hash]) location.replace(legacyAnchors[location.hash]);
  };
  redirectLegacyAnchor();
  window.addEventListener('hashchange', redirectLegacyAnchor);

  // Ano do rodapé (o HTML já traz um valor estático como fallback).
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // Borda do cabeçalho ao rolar.
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-scrolled', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // Menu no celular.
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('menu-principal');
  if (toggle && nav) {
    var label = toggle.querySelector('.sr-only');
    var setOpen = function (open) {
      nav.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', String(open));
      if (label) label.textContent = open ? T.closeMenu : T.openMenu;
    };

    toggle.addEventListener('click', function () {
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });
    nav.addEventListener('click', function (event) {
      if (event.target.closest('a')) setOpen(false);
    });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        toggle.focus();
      }
    });
    document.addEventListener('click', function (event) {
      if (toggle.getAttribute('aria-expanded') === 'true' && !header.contains(event.target)) {
        setOpen(false);
      }
    });
    window.matchMedia('(min-width: 1101px)').addEventListener('change', function (mq) {
      if (mq.matches) setOpen(false);
    });
  }

  // Aviso de cookies: o Google Analytics só é carregado depois de "Aceitar"
  // (o carregador fica no <head> de cada página, em window.loadAnalytics).
  var CONSENT_KEY = 'perovano-cookies';
  var readConsent = function () {
    try { return localStorage.getItem(CONSENT_KEY); } catch (e) { return null; }
  };
  var saveConsent = function (value) {
    try { localStorage.setItem(CONSENT_KEY, value); } catch (e) { /* sem armazenamento: vale só nesta visita */ }
  };
  var clearAnalyticsCookies = function () {
    var host = location.hostname;
    var domains = ['', host, '.' + host, '.' + host.split('.').slice(-3).join('.')];
    document.cookie.split(';').forEach(function (cookie) {
      var name = cookie.split('=')[0].trim();
      if (!/^_ga/.test(name) && name !== '_gid') return;
      domains.forEach(function (domain) {
        document.cookie = name + '=; Max-Age=0; path=/' + (domain ? '; domain=' + domain : '');
      });
    });
  };

  var banner = null;
  var closeBanner = function () {
    if (!banner) return;
    banner.remove();
    banner = null;
  };
  var openBanner = function (focus) {
    if (banner) return;
    banner = document.createElement('section');
    banner.className = 'cookie-banner';
    banner.setAttribute('aria-labelledby', 'cookie-titulo');
    banner.innerHTML =
      '<h2 class="cookie-banner__title" id="cookie-titulo">' + T.cookieTitle + '</h2>' +
      '<p class="cookie-banner__text">' + T.cookieText + '</p>' +
      '<div class="cookie-banner__actions">' +
      '<button type="button" class="btn btn--primary btn--small" data-consent="aceito">' + T.accept + '</button>' +
      '<button type="button" class="btn btn--secondary btn--small" data-consent="recusado">' + T.decline + '</button>' +
      '</div>';
    banner.addEventListener('click', function (event) {
      var button = event.target.closest('[data-consent]');
      if (!button) return;
      var value = button.getAttribute('data-consent');
      var previous = readConsent();
      saveConsent(value);
      closeBanner();
      if (value === 'aceito') {
        if (typeof window.loadAnalytics === 'function') window.loadAnalytics();
      } else {
        if (typeof window.gtag === 'function') window.gtag('consent', 'update', { analytics_storage: 'denied' });
        clearAnalyticsCookies();
        // Se o Analytics já estava rodando nesta página, recarrega para desligá-lo de vez.
        if (previous === 'aceito' && window.__gaLoaded) location.reload();
      }
    });
    document.body.appendChild(banner);
    if (focus) banner.querySelector('button').focus();
  };

  if (readConsent() !== 'aceito' && readConsent() !== 'recusado') openBanner(false);

  // Rodapé: permite rever a escolha a qualquer momento.
  document.querySelectorAll('.site-footer__bottom').forEach(function (bottom) {
    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'link-button';
    button.textContent = T.cookiePrefs;
    button.addEventListener('click', function () { openBanner(true); });
    var holder = document.createElement('p');
    holder.appendChild(button);
    bottom.appendChild(holder);
  });

  // Analytics: cliques em WhatsApp e e-mail viram conversões (evento generate_lead do GA4).
  // Só registra quando o Analytics foi autorizado e carregado.
  document.addEventListener('click', function (event) {
    var link = event.target.closest && event.target.closest('a[href]');
    if (!link || !window.__gaLoaded || typeof window.gtag !== 'function') return;
    var href = link.getAttribute('href');
    var method = /wa\.me\//.test(href) ? 'whatsapp' : /^mailto:/.test(href) ? 'email' : '';
    if (!method) return;
    var section = link.closest('section, header, footer');
    window.gtag('event', 'generate_lead', {
      method: method,
      link_text: (link.textContent || '').trim().slice(0, 100),
      page_location: location.href,
      cta_section: section ? (section.id || section.className.split(' ')[0]) : ''
    });
  });

  // Blog: filtro por categoria + busca. Sem JS, os chips levam às páginas de cada categoria.
  var chips = Array.prototype.slice.call(document.querySelectorAll('.chip[data-filter]'));
  var groups = Array.prototype.slice.call(document.querySelectorAll('.blog-group'));
  if (chips.length && groups.length) {
    var searchBox = document.querySelector('.blog-search');
    var searchInput = document.getElementById('busca-artigos');
    var emptyMsg = document.querySelector('.blog-empty');
    var state = { category: '', query: '' };
    var normalize = function (text) {
      return text.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    };
    var apply = function () {
      var terms = normalize(state.query).split(/\s+/).filter(Boolean);
      var total = 0;
      groups.forEach(function (group) {
        var visible = 0;
        var inCategory = !state.category || group.getAttribute('data-category') === state.category;
        group.querySelectorAll('.post-card').forEach(function (card) {
          var haystack = normalize(card.getAttribute('data-search') || card.textContent);
          var match = inCategory && terms.every(function (t) { return haystack.indexOf(t) !== -1; });
          card.hidden = !match;
          if (match) visible++;
        });
        group.hidden = visible === 0;
        total += visible;
      });
      chips.forEach(function (chip) {
        chip.setAttribute('aria-pressed', String(chip.getAttribute('data-filter') === state.category));
      });
      if (emptyMsg) {
        emptyMsg.hidden = total !== 0;
        emptyMsg.textContent = total === 0
          ? T.searchEmpty(state.query)
          : '';
      }
    };
    chips.forEach(function (chip) {
      chip.addEventListener('click', function (event) {
        event.preventDefault();
        state.category = chip.getAttribute('data-filter');
        apply();
        history.replaceState(null, '', state.category ? chip.getAttribute('data-anchor') : location.pathname);
      });
    });
    if (searchBox && searchInput) {
      searchBox.hidden = false;
      searchInput.addEventListener('input', function () {
        state.query = searchInput.value.trim();
        apply();
      });
    }
    var initial = chips.filter(function (chip) { return chip.getAttribute('data-anchor') === location.hash; })[0];
    state.category = initial ? initial.getAttribute('data-filter') : '';
    apply();
  }

  // Artigo: destaca no índice a seção em leitura.
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.post__toc a[href^="#"]'));
  if (tocLinks.length && 'IntersectionObserver' in window) {
    var byId = {};
    tocLinks.forEach(function (a) { byId[a.getAttribute('href').slice(1)] = a; });
    var tocObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        tocLinks.forEach(function (a) { a.removeAttribute('aria-current'); });
        var link = byId[entry.target.id];
        if (link) link.setAttribute('aria-current', 'true');
      });
    }, { rootMargin: '0px 0px -70% 0px' });
    Object.keys(byId).forEach(function (id) {
      var heading = document.getElementById(id);
      if (heading) tocObserver.observe(heading);
    });
  }

  // Soluções: o texto em foco escolhe a cena do palco.
  var solutionItems = Array.prototype.slice.call(document.querySelectorAll('.solution-item[data-scene]'));
  var scenes = Array.prototype.slice.call(document.querySelectorAll('.showcase__stage .scene[data-scene]'));
  // No celular e no tablet cada item ganha a sua própria cena (cópia decorativa);
  // ela anima quando aparece na tela.
  var inlineScenes = [];
  solutionItems.forEach(function (item) {
    var source = scenes.filter(function (sc) { return sc.getAttribute('data-scene') === item.getAttribute('data-scene'); })[0];
    if (!source) return;
    var holder = document.createElement('div');
    holder.className = 'solution-item__stage';
    holder.setAttribute('aria-hidden', 'true');
    var clone = source.cloneNode(true);
    clone.classList.remove('is-active');
    holder.appendChild(clone);
    item.insertBefore(holder, item.firstChild);
    inlineScenes.push(clone);
  });
  if (solutionItems.length && scenes.length && 'IntersectionObserver' in window) {
    var countUp = function (scene) {
      if (reduceMotion) return;
      scene.querySelectorAll('[data-count]').forEach(function (el) {
        var target = parseInt(el.getAttribute('data-count'), 10);
        var start = null;
        var step = function (ts) {
          if (start === null) start = ts;
          var t = Math.min(1, (ts - start) / 1100);
          el.textContent = Math.round(target * (1 - Math.pow(1 - t, 3)));
          if (t < 1) window.requestAnimationFrame(step);
        };
        window.requestAnimationFrame(step);
      });
    };
    var activate = function (name) {
      solutionItems.forEach(function (item) {
        item.classList.toggle('is-active', item.getAttribute('data-scene') === name);
      });
      scenes.forEach(function (scene) {
        var on = scene.getAttribute('data-scene') === name;
        if (on && !scene.classList.contains('is-active')) {
          scene.classList.add('is-active');
          countUp(scene);
        } else if (!on) {
          scene.classList.remove('is-active');
        }
      });
    };
    var sceneObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) activate(entry.target.getAttribute('data-scene'));
      });
    }, { rootMargin: '-50% 0px -40% 0px' });
    solutionItems.forEach(function (item) { sceneObserver.observe(item); });

    var inlineObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting || entry.target.classList.contains('is-active')) return;
        entry.target.classList.add('is-active');
        countUp(entry.target);
      });
    }, { threshold: 0.55 });
    inlineScenes.forEach(function (scene) { inlineObserver.observe(scene); });
  }

  if (reduceMotion) return;

  // Manifesto: as palavras acendem conforme a frase atravessa a tela.
  var manifesto = document.querySelector('[data-words]');
  var words = [];
  if (manifesto) {
    var text = manifesto.textContent.trim();
    manifesto.setAttribute('aria-label', text);
    manifesto.innerHTML = text.split(/\s+/).map(function (w) {
      return '<span class="w" aria-hidden="true">' + w + '</span>';
    }).join(' ');
    words = Array.prototype.slice.call(manifesto.querySelectorAll('.w'));
  }

  // Como trabalhamos: a linha do tempo se desenha e as etapas acendem.
  var stepsList = document.querySelector('.steps');
  var steps = stepsList ? Array.prototype.slice.call(stepsList.querySelectorAll('.step')) : [];

  var scrollTicking = false;
  var onScrollEffects = function () {
    scrollTicking = false;
    var vh = window.innerHeight;
    if (words.length) {
      var r = manifesto.getBoundingClientRect();
      var p = (vh * 0.85 - r.top) / (r.height + vh * 0.35);
      var lit = Math.max(0, Math.min(1, p)) * words.length * 1.1;
      words.forEach(function (w, i) {
        w.style.opacity = (0.16 + 0.84 * Math.max(0, Math.min(1, lit - i))).toFixed(2);
      });
    }
    if (steps.length) {
      var sr = stepsList.getBoundingClientRect();
      var progress = Math.max(0, Math.min(1, (vh * 0.8 - sr.top) / (vh * 0.45)));
      stepsList.style.setProperty('--progress', progress.toFixed(3));
      var horizontal = window.matchMedia('(min-width: 1025px)').matches;
      steps.forEach(function (step, i) {
        var lit = horizontal
          ? progress >= (i + 0.35) / steps.length
          : step.getBoundingClientRect().top < vh * 0.75;
        step.classList.toggle('is-lit', lit);
      });
    }
  };
  var requestScrollEffects = function () {
    if (!scrollTicking) { scrollTicking = true; window.requestAnimationFrame(onScrollEffects); }
  };
  if (words.length || steps.length) {
    onScrollEffects();
    window.addEventListener('scroll', requestScrollEffects, { passive: true });
    window.addEventListener('resize', requestScrollEffects);
  }

  // Parede da abertura: inclina levemente seguindo o ponteiro (apenas mouse).
  var hero = document.querySelector('.hero');
  var plane = document.querySelector('.wall__plane');
  if (hero && plane && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    hero.addEventListener('pointermove', function (event) {
      var r = hero.getBoundingClientRect();
      var x = (event.clientX - r.left) / r.width - 0.5;
      var y = (event.clientY - r.top) / r.height - 0.5;
      plane.style.setProperty('--tilt-x', (38 - y * 6).toFixed(2) + 'deg');
      plane.style.setProperty('--tilt-y', (x * 6).toFixed(2) + 'deg');
    });
    hero.addEventListener('pointerleave', function () {
      plane.style.removeProperty('--tilt-x');
      plane.style.removeProperty('--tilt-y');
    });
  }

  // Portfólio: cada janela percorre o site real conforme a rolagem.
  var frames = Array.prototype.slice.call(document.querySelectorAll('[data-pan]'));
  if (!frames.length) return;

  var items = frames.map(function (frame) {
    return { screen: frame.querySelector('.work__screen'), img: frame.querySelector('.work__screen img'), visible: false };
  }).filter(function (item) { return item.screen && item.img; });

  var ticking = false;
  var update = function () {
    ticking = false;
    var vh = window.innerHeight;
    items.forEach(function (item) {
      if (!item.visible) return;
      var r = item.screen.getBoundingClientRect();
      var distance = item.img.offsetHeight - item.screen.clientHeight;
      if (distance <= 0) return;
      // 0 quando a janela entra por baixo; 1 quando chega ao terço superior da tela.
      var progress = (vh - r.top) / (vh * 0.85 + r.height * 0.4);
      progress = Math.min(1, Math.max(0, progress));
      var eased = progress < 0.5 ? 2 * progress * progress : 1 - Math.pow(-2 * progress + 2, 2) / 2;
      item.img.style.transform = 'translate3d(0,' + (-eased * distance).toFixed(1) + 'px,0)';
    });
  };
  var requestUpdate = function () {
    if (!ticking) { ticking = true; window.requestAnimationFrame(update); }
  };

  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        items.forEach(function (item) {
          if (item.screen === entry.target) item.visible = entry.isIntersecting;
        });
      });
      requestUpdate();
    }, { rootMargin: '10% 0px' });
    items.forEach(function (item) { observer.observe(item.screen); });
  } else {
    items.forEach(function (item) { item.visible = true; });
  }

  window.addEventListener('scroll', requestUpdate, { passive: true });
  window.addEventListener('resize', requestUpdate);
  items.forEach(function (item) { item.img.addEventListener('load', requestUpdate); });
})();
