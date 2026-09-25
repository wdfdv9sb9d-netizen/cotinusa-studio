const toggle=document.querySelector('.menu-toggle');const nav=document.querySelector('.site-nav');toggle.addEventListener('click',()=>{const open=nav.classList.toggle('open');toggle.setAttribute('aria-expanded',String(open));toggle.textContent=open?'Cerrar':'Menú'});document.querySelectorAll('.site-nav a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.textContent='Menú'}));
const io=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('is-visible');io.unobserve(entry.target)}})},{threshold:.1});document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
const projects={
'01':{
  title:'FKS — Fat King Spacial',
  text:'Una identidad de basketball y streetwear construida alrededor de poder, presencia y ambición. FKS combina producto, cultura urbana y dirección visual dentro de un universo de marca reconocible.',
  tags:[
    'Brand Identity',
    'Art Direction',
    'Sneakers',
    'Streetwear',
    'Campaign'
  ],
  focus:'Construir una marca con personalidad propia capaz de vivir en sneakers, apparel, packaging, campañas y experiencias digitales.',
  result:'Un universo visual oscuro, premium y contundente, articulado mediante la corona FKS, negro, rojo y oro, fotografía urbana y el concepto “From the streets to the stars”.'
},
'02':{title:'Lúmina Skin',text:'Concepto de marca para cuidado facial con un lenguaje cálido, simple y reconocible. El proyecto explora identidad, packaging y una landing editorial para lanzamiento.',tags:['Identidad','Packaging','Landing'],focus:'Crear una marca de skincare cercana y refinada, capaz de destacar en un mercado visualmente saturado.',result:'Una identidad suave con contraste editorial, formas orgánicas y un lenguaje digital muy limpio.'},
'03':{title:'Forma Construct',text:'Sistema digital para una empresa de construcción que quiere comunicar precisión y confianza. La propuesta ordena servicios complejos dentro de una experiencia web clara.',tags:['Web','Sistema gráfico','Contenido'],focus:'Transformar una empresa técnica en una marca más comprensible, ordenada y contemporánea.',result:'Arquitectura de contenidos clara, tipografía contundente y un sistema visual modular.'},
'04':{title:'Tèrra Cocina',text:'Identidad conceptual para un restaurante de cocina honesta. Tipografía expresiva, color reconocible y una web centrada en carta, reservas y personalidad de marca.',tags:['Marca','Menú','Web'],focus:'Transmitir cocina de temporada y personalidad sin recurrir a una estética gastronómica previsible.',result:'Una identidad expresiva, directa y adaptable a carta, señalética, social y web.'}}
const modal=document.querySelector('#project-modal'),modalTitle=document.querySelector('#modal-title'),modalText=document.querySelector('#modal-text'),modalTags=document.querySelector('#modal-tags'),modalFocus=document.querySelector('#modal-focus'),modalResult=document.querySelector('#modal-result');document.querySelectorAll('.project-card').forEach(card=>{const openProject=()=>{const d=projects[card.dataset.project];modalTitle.textContent=d.title;modalText.textContent=d.text;modalTags.innerHTML=d.tags.map(t=>`<span>${t}</span>`).join('');modalFocus.textContent=d.focus;modalResult.textContent=d.result;modal.showModal()};card.addEventListener('click',openProject);card.querySelector('.project-open').addEventListener('click',e=>{e.stopPropagation();openProject()})});document.querySelector('.modal-close').addEventListener('click',()=>modal.close());modal.addEventListener('click',e=>{const r=modal.getBoundingClientRect();const inside=e.clientX>=r.left&&e.clientX<=r.right&&e.clientY>=r.top&&e.clientY<=r.bottom;if(!inside)modal.close()});
