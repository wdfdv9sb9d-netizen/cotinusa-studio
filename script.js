const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.site-nav');

if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
    toggle.textContent = open ? 'Cerrar' : 'Menú';
  });

  document.querySelectorAll('.site-nav a').forEach(a => {
    a.addEventListener('click', () => {
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.textContent = 'Menú';
    });
  });
}


/* ANIMACIONES */

const io = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-visible');
      io.unobserve(entry.target);
    }
  });
}, {
  threshold: .1
});

document.querySelectorAll('.reveal').forEach(el => io.observe(el));


/* PROYECTOS CON MODAL */

const projects = {

  '02': {
    title: 'Lúmina Skin',
    text: 'Concepto de marca para cuidado facial con un lenguaje cálido, simple y reconocible. El proyecto explora identidad, packaging y una landing editorial para lanzamiento.',
    tags: ['Identidad', 'Packaging', 'Landing'],
    focus: 'Crear una marca de skincare cercana y refinada, capaz de destacar en un mercado visualmente saturado.',
    result: 'Una identidad suave con contraste editorial, formas orgánicas y un lenguaje digital muy limpio.'
  },

  '03': {
    title: 'Forma Construct',
    text: 'Sistema digital para una empresa de construcción que quiere comunicar precisión y confianza. La propuesta ordena servicios complejos dentro de una experiencia web clara.',
    tags: ['Web', 'Sistema gráfico', 'Contenido'],
    focus: 'Transformar una empresa técnica en una marca más comprensible, ordenada y contemporánea.',
    result: 'Arquitectura de contenidos clara, tipografía contundente y un sistema visual modular.'
  },

  '04': {
    title: 'Tèrra Cocina',
    text: 'Identidad conceptual para un restaurante de cocina honesta. Tipografía expresiva, color reconocible y una web centrada en carta, reservas y personalidad de marca.',
    tags: ['Marca', 'Menú', 'Web'],
    focus: 'Transmitir cocina de temporada y personalidad sin recurrir a una estética gastronómica previsible.',
    result: 'Una identidad expresiva, directa y adaptable a carta, señalética, social y web.'
  }

};


/* MODAL */

const modal = document.querySelector('#project-modal');
const modalTitle = document.querySelector('#modal-title');
const modalText = document.querySelector('#modal-text');
const modalTags = document.querySelector('#modal-tags');
const modalFocus = document.querySelector('#modal-focus');
const modalResult = document.querySelector('#modal-result');


document.querySelectorAll('.project-card').forEach(card => {

  const projectId = card.dataset.project;

  /* FKS TIENE SU PROPIA PÁGINA */

  if (projectId === 'fks') {

    card.addEventListener('click', e => {

      if (e.target.closest('a')) return;

      window.location.href = 'proyectos/fks/';
    });

    return;
  }


  /* RESTO DE PROYECTOS */

  const openProject = () => {

    const d = projects[projectId];

    if (!d || !modal) return;

    modalTitle.textContent = d.title;
    modalText.textContent = d.text;

    modalTags.innerHTML = d.tags
      .map(t => `<span>${t}</span>`)
      .join('');

    modalFocus.textContent = d.focus;
    modalResult.textContent = d.result;

    modal.showModal();
  };


  card.addEventListener('click', openProject);

  const button = card.querySelector('.project-open');

  if (button) {
    button.addEventListener('click', e => {
      e.stopPropagation();
      openProject();
    });
  }

});


/* CERRAR MODAL */

const closeButton = document.querySelector('.modal-close');

if (closeButton && modal) {

  closeButton.addEventListener('click', () => {
    modal.close();
  });

  modal.addEventListener('click', e => {

    const r = modal.getBoundingClientRect();

    const inside =
      e.clientX >= r.left &&
      e.clientX <= r.right &&
      e.clientY >= r.top &&
      e.clientY <= r.bottom;

    if (!inside) modal.close();

  });

}
