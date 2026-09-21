/* ==========================================================================
   Espacio Mañío — Interactive Application Logic
   Features: Drone Video Controls, WhatsApp Quoting Engine, PWA & Native Share,
             Gallery Lightbox Modal, Mobile Navigation
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  const WHATSAPP_MAIN = '56988886174';
  const SITE_URL = 'https://dinogonzalez.github.io/espaciomanio/';
  const SITE_TITLE = 'Espacio Mañío — Paseos & Eventos Privados en Talagante';
  const SITE_TEXT = 'Recinto 100% exclusivo para eventos, paseos de fin de año y empresas. Piscina de 15x7m, quincho y áreas verdes.';

  // 1. Set Minimum Date for Reservation to Today
  const dateInput = document.getElementById('fechaEvento');
  if (dateInput) {
    const today = new Date().toISOString().split('T')[0];
    dateInput.min = today;
  }

  // 2. Navbar Scroll Dynamic Effect
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });

  // 3. Mobile Hamburger Menu Toggle
  const hamburgerBtn = document.getElementById('hamburgerBtn');
  const navMenuWrapper = document.getElementById('navMenuWrapper');
  if (hamburgerBtn && navMenuWrapper) {
    hamburgerBtn.addEventListener('click', () => {
      navMenuWrapper.classList.toggle('active');
    });

    // Close menu when clicking on any link
    navMenuWrapper.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        navMenuWrapper.classList.remove('active');
      });
    });
  }

  // 4. Drone Cinema Video Controls
  const droneVideo = document.getElementById('droneVideo');
  const videoPlayPauseBtn = document.getElementById('videoPlayPauseBtn');
  const videoSoundBtn = document.getElementById('videoSoundBtn');
  const videoFullscreenBtn = document.getElementById('videoFullscreenBtn');

  if (droneVideo) {
    // Ensure video plays automatically muted
    droneVideo.muted = true;
    droneVideo.play().catch(() => {
      // Browser prevented autoplay, user can click play
    });

    // Play / Pause Toggle
    if (videoPlayPauseBtn) {
      videoPlayPauseBtn.addEventListener('click', () => {
        if (droneVideo.paused) {
          droneVideo.play();
          videoPlayPauseBtn.innerHTML = '<i class="fa-solid fa-pause"></i> <span>Pausar</span>';
        } else {
          droneVideo.pause();
          videoPlayPauseBtn.innerHTML = '<i class="fa-solid fa-play"></i> <span>Reproducir</span>';
        }
      });
    }

    // Sound Toggle (Mute / Unmute)
    if (videoSoundBtn) {
      videoSoundBtn.addEventListener('click', () => {
        droneVideo.muted = !droneVideo.muted;
        if (droneVideo.muted) {
          videoSoundBtn.innerHTML = '<i class="fa-solid fa-volume-xmark"></i> <span>Activar Sonido</span>';
        } else {
          videoSoundBtn.innerHTML = '<i class="fa-solid fa-volume-high"></i> <span>Silenciar</span>';
        }
      });
    }

    // Fullscreen Toggle
    if (videoFullscreenBtn) {
      videoFullscreenBtn.addEventListener('click', () => {
        if (droneVideo.requestFullscreen) {
          droneVideo.requestFullscreen();
        } else if (droneVideo.webkitRequestFullscreen) {
          droneVideo.webkitRequestFullscreen();
        } else if (droneVideo.msRequestFullscreen) {
          droneVideo.msRequestFullscreen();
        }
      });
    }
  }

  // 5. Native Share API & Clipboard Fallback
  function triggerShare() {
    if (navigator.share) {
      navigator.share({
        title: SITE_TITLE,
        text: SITE_TEXT,
        url: SITE_URL
      }).catch((err) => {
        if (err.name !== 'AbortError') {
          copyToClipboard(SITE_URL);
        }
      });
    } else {
      copyToClipboard(SITE_URL);
    }
  }

  function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
      showToast('¡Enlace de Espacio Mañío copiado al portapapeles!');
    }).catch(() => {
      showToast('Enlace: ' + text);
    });
  }

  function showToast(msg) {
    const toast = document.getElementById('toastNotification');
    if (toast) {
      toast.textContent = msg;
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, 3200);
    }
  }

  const shareSiteBtn = document.getElementById('shareSiteBtn');
  const mobileShareBtn = document.getElementById('mobileShareBtn');
  if (shareSiteBtn) shareSiteBtn.addEventListener('click', triggerShare);
  if (mobileShareBtn) mobileShareBtn.addEventListener('click', triggerShare);

  // 6. Interactive WhatsApp Quoting Engine
  const bookingForm = document.getElementById('bookingForm');
  if (bookingForm) {
    bookingForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const fecha = document.getElementById('fechaEvento').value;
      const tipo = document.getElementById('tipoEvento').value;
      const personas = document.getElementById('cantidadPersonas').value;
      const nombre = document.getElementById('nombreCliente').value.trim();
      const notas = document.getElementById('notasCliente').value.trim();

      if (!fecha) {
        alert('Por favor selecciona la fecha deseada de tu evento.');
        return;
      }

      // Format Date nicely (DD/MM/AAAA)
      const dateParts = fecha.split('-');
      const dateFormatted = `${dateParts[2]}/${dateParts[1]}/${dateParts[0]}`;

      let msg = `Hola *Espacio Mañío* 👋🏻, quisiera consultar valores y disponibilidad para un evento:\n\n`;
      msg += `📅 *Fecha solicitada*: ${dateFormatted}\n`;
      msg += `🎉 *Tipo de evento*: ${tipo}\n`;
      msg += `👥 *Cantidad de asistentes*: ${personas}\n`;
      if (nombre) msg += `👤 *Nombre cliente*: ${nombre}\n`;
      if (notas) msg += `📝 *Comentarios/Requerimientos*: ${notas}\n`;
      msg += `\n📍 *Ubicación*: Lonquén Sur, Paradero 38 1/2, Talagante\n`;
      msg += `🌐 *Web*: ${SITE_URL}\n\n`;
      msg += `Quedo atento(a) a su pronta respuesta. ¡Muchas gracias!`;

      const encodedMsg = encodeURIComponent(msg);
      const whatsappUrl = `https://wa.me/${WHATSAPP_MAIN}?text=${encodedMsg}`;
      window.open(whatsappUrl, '_blank');
    });
  }

  // 7. Gallery Lightbox Modal
  const imageModal = document.getElementById('imageModal');
  const modalImage = document.getElementById('modalImage');
  const modalCaption = document.getElementById('modalCaption');
  const modalClose = document.getElementById('modalClose');

  document.querySelectorAll('.gallery-item').forEach(item => {
    item.addEventListener('click', () => {
      const imgSrc = item.getAttribute('data-img');
      const caption = item.getAttribute('data-caption');

      if (imageModal && modalImage) {
        modalImage.src = imgSrc;
        modalCaption.textContent = caption || 'Espacio Mañío — Talagante';
        imageModal.classList.add('active');
        imageModal.setAttribute('aria-hidden', 'false');
      }
    });
  });

  if (modalClose && imageModal) {
    modalClose.addEventListener('click', () => {
      imageModal.classList.remove('active');
      imageModal.setAttribute('aria-hidden', 'true');
    });

    imageModal.addEventListener('click', (e) => {
      if (e.target === imageModal) {
        imageModal.classList.remove('active');
        imageModal.setAttribute('aria-hidden', 'true');
      }
    });
  }
});
