// Study Hub TI — interações do portfólio (GitHub Pages)

(function () {
  var root = document.documentElement;

  // ---------- Tema claro/escuro ----------
  // A preferência do visitante fica no localStorage; sem ela, vale a do sistema.
  try {
    var salvo = localStorage.getItem('tema');
    if (salvo === 'light' || salvo === 'dark') root.setAttribute('data-theme', salvo);
  } catch (e) { /* armazenamento indisponível: segue o tema do sistema */ }

  var botaoTema = document.getElementById('theme-toggle');
  if (botaoTema) {
    botaoTema.addEventListener('click', function () {
      var atual = root.getAttribute('data-theme') ||
        (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
      var novo = atual === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', novo);
      try { localStorage.setItem('tema', novo); } catch (e) { /* ignora */ }
    });
  }

  // ---------- Menu mobile ----------
  var botaoMenu = document.getElementById('menu-toggle');
  var nav = document.getElementById('site-nav');
  if (botaoMenu && nav) {
    botaoMenu.addEventListener('click', function () {
      var aberto = nav.classList.toggle('open');
      botaoMenu.setAttribute('aria-expanded', String(aberto));
      botaoMenu.setAttribute('aria-label', aberto ? 'Fechar menu' : 'Abrir menu');
    });
    nav.addEventListener('click', function (evento) {
      if (evento.target.tagName === 'A') {
        nav.classList.remove('open');
        botaoMenu.setAttribute('aria-expanded', 'false');
        botaoMenu.setAttribute('aria-label', 'Abrir menu');
      }
    });
  }

  // ---------- Destaque da seção visível no menu ----------
  var links = nav ? nav.querySelectorAll('a[href^="#"]') : [];
  if ('IntersectionObserver' in window && links.length) {
    var porId = {};
    links.forEach(function (link) { porId[link.getAttribute('href').slice(1)] = link; });

    var observador = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (entrada) {
        if (!entrada.isIntersecting) return;
        links.forEach(function (link) { link.classList.remove('active'); });
        var ativo = porId[entrada.target.id];
        if (ativo) ativo.classList.add('active');
      });
    }, { rootMargin: '-45% 0px -50% 0px' });

    // O topo não tem link no menu: ao voltar para ele, nenhum item fica destacado.
    Object.keys(porId).concat('topo').forEach(function (id) {
      var secao = document.getElementById(id);
      if (secao) observador.observe(secao);
    });
  }

  // ---------- Ano no rodapé ----------
  var ano = document.getElementById('year');
  if (ano) ano.textContent = String(new Date().getFullYear());
})();
