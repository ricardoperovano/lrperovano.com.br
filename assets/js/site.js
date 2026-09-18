// PEROVANO — comportamento do site. Tudo aqui é melhoria progressiva:
// sem JS o conteúdo, os links e a navegação continuam funcionando.
(function () {
  'use strict';

  var root = document.documentElement;
  root.classList.add('js');

  // Âncoras do site anterior que podem ter links externos.
  var legacyAnchors = { '#servicos': '#solucoes', '#top': '#inicio' };
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
      if (label) label.textContent = open ? 'Fechar menu' : 'Abrir menu';
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
    window.matchMedia('(min-width: 881px)').addEventListener('change', function (mq) {
      if (mq.matches) setOpen(false);
    });
  }

  // Entrada discreta das seções.
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var targets = document.querySelectorAll('.reveal');
  if (!reduceMotion && 'IntersectionObserver' in window && targets.length) {
    root.classList.add('motion-ok');
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    targets.forEach(function (el) { observer.observe(el); });
  }
})();
