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
  const videoFullscreenBtn = document.getElementById('videoFullscreenBtn');

  if (droneVideo) {
    // Ensure video plays automatically muted (drone footage has no audio track)
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

  // 5. Share Modal & Official QR Controller
  const shareModal = document.getElementById('shareModal');
  const shareModalClose = document.getElementById('shareModalClose');
  const shareSiteBtn = document.getElementById('shareSiteBtn');
  const mobileShareBtn = document.getElementById('mobileShareBtn');
  const copyShareTextBtn = document.getElementById('copyShareTextBtn');

  const INVITATION_TEXT = `ESPACIO MAÑÍO — Paseos & Eventos Privados
Lonquén Sur, Paradero 38 ½, Talagante

Recinto 100% exclusivo para grupos, empresas y colegios.

Instalaciones y servicios incluidos:
• Espectacular Piscina de 15x7 metros (105 m² de agua cristalina)
• Quincho techado equipado con parrillas para asados
• Más de 5.000 m² de áreas verdes y sombra natural
• Estacionamiento privado cerrado para más de 30 vehículos
• Baños higienizados y camarines
• Jornada de arriendo: 10:00 a 18:30 horas

Contacto y Reservas: +56 9 8888 6174
Sitio Web Oficial: https://dinogonzalez.github.io/espaciomanio/`;

  function openShareModal() {
    if (shareModal) {
      shareModal.classList.add('active');
      shareModal.setAttribute('aria-hidden', 'false');
    }
  }

  function closeShareModal() {
    if (shareModal) {
      shareModal.classList.remove('active');
      shareModal.setAttribute('aria-hidden', 'true');
    }
  }

  if (shareSiteBtn) {
    shareSiteBtn.addEventListener('click', (e) => {
      e.preventDefault();
      openShareModal();
    });
  }

  if (mobileShareBtn) {
    mobileShareBtn.addEventListener('click', (e) => {
      e.preventDefault();
      openShareModal();
    });
  }

  if (shareModalClose) {
    shareModalClose.addEventListener('click', closeShareModal);
  }

  if (shareModal) {
    shareModal.addEventListener('click', (e) => {
      if (e.target === shareModal) {
        closeShareModal();
      }
    });
  }

  if (copyShareTextBtn) {
    copyShareTextBtn.addEventListener('click', () => {
      navigator.clipboard.writeText(INVITATION_TEXT).then(() => {
        showToast('Invitación corporativa copiada al portapapeles');
      }).catch(() => {
        showToast('Texto copiado');
      });
    });
  }

  // QR Selection Tab Switching (Web QR vs WhatsApp QR)
  const tabWebQrBtn = document.getElementById('tabWebQrBtn');
  const tabWhatsappQrBtn = document.getElementById('tabWhatsappQrBtn');
  const panelWebQr = document.getElementById('panelWebQr');
  const panelWhatsappQr = document.getElementById('panelWhatsappQr');

  if (tabWebQrBtn && tabWhatsappQrBtn && panelWebQr && panelWhatsappQr) {
    tabWebQrBtn.addEventListener('click', () => {
      tabWebQrBtn.classList.add('active');
      tabWhatsappQrBtn.classList.remove('active');
      panelWebQr.classList.add('active');
      panelWhatsappQr.classList.remove('active');
    });

    tabWhatsappQrBtn.addEventListener('click', () => {
      tabWhatsappQrBtn.classList.add('active');
      tabWebQrBtn.classList.remove('active');
      panelWhatsappQr.classList.add('active');
      panelWebQr.classList.remove('active');
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

  // 6. Interactive WhatsApp Quoting Engine & Modal Controller
  const quoteModal = document.getElementById('quoteModal');
  const quoteModalClose = document.getElementById('quoteModalClose');
  const modalFechaEvento = document.getElementById('modalFechaEvento');

  if (modalFechaEvento) {
    const today = new Date().toISOString().split('T')[0];
    modalFechaEvento.min = today;
  }

  function openQuoteModal() {
    if (quoteModal) {
      quoteModal.classList.add('active');
      quoteModal.setAttribute('aria-hidden', 'false');
      // Autofocus date input
      setTimeout(() => {
        if (modalFechaEvento) {
          modalFechaEvento.focus();
          if (modalFechaEvento.showPicker) {
            try { modalFechaEvento.showPicker(); } catch (_) {}
          }
        }
      }, 150);
    }
  }

  function closeQuoteModal() {
    if (quoteModal) {
      quoteModal.classList.remove('active');
      quoteModal.setAttribute('aria-hidden', 'true');
    }
  }

  // Attach click listener to all buttons that trigger the quote modal
  document.querySelectorAll('.open-quote-modal').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openQuoteModal();
    });
  });

  if (quoteModalClose) {
    quoteModalClose.addEventListener('click', closeQuoteModal);
  }

  if (quoteModal) {
    quoteModal.addEventListener('click', (e) => {
      if (e.target === quoteModal) {
        closeQuoteModal();
      }
    });
  }

  // Universal WhatsApp message builder and launcher
  function sendQuoteToWhatsApp({ fecha, tipo, personas, nombre, notas, source }) {
    if (!fecha) {
      alert('Por favor selecciona la fecha deseada de tu evento.');
      return;
    }

    // Format Date nicely (DD/MM/AAAA)
    const dateParts = fecha.split('-');
    const dateFormatted = `${dateParts[2]}/${dateParts[1]}/${dateParts[0]}`;

    let msg = `Estimados administradores de *Espacio Mañío*:\n\n`;
    msg += `Quisiera consultar disponibilidad y valores oficiales para el siguiente evento:\n\n`;
    msg += `• *Fecha solicitada*: ${dateFormatted}\n`;
    msg += `• *Tipo de evento*: ${tipo}\n`;
    msg += `• *Cantidad de asistentes*: ${personas}\n`;
    if (nombre) msg += `• *Nombre del solicitante*: ${nombre}\n`;
    if (notas) msg += `• *Consultas / Requerimientos*: ${notas}\n`;
    msg += `• *Recinto*: Lonquén Sur, Paradero 38 1/2, Talagante\n`;
    msg += `• *Sitio Web*: ${SITE_URL}\n\n`;
    msg += `Agradezco de antemano su pronta respuesta y cotización formal.`;

    const encodedMsg = encodeURIComponent(msg);
    const whatsappUrl = `https://wa.me/${WHATSAPP_MAIN}?text=${encodedMsg}`;

    // Popup-safe opening: try window.open, fallback to location.href if blocked
    const win = window.open(whatsappUrl, '_blank');
    if (!win || win.closed || typeof win.closed === 'undefined') {
      window.location.href = whatsappUrl;
    }

    if (source === 'modal') {
      closeQuoteModal();
    }
    showToast('Abriendo WhatsApp para enviar tu cotización...');
  }

  // Handler for Inline Form on Page
  const bookingForm = document.getElementById('bookingForm');
  if (bookingForm) {
    bookingForm.addEventListener('submit', (e) => {
      e.preventDefault();
      sendQuoteToWhatsApp({
        fecha: document.getElementById('fechaEvento').value,
        tipo: document.getElementById('tipoEvento').value,
        personas: document.getElementById('cantidadPersonas').value,
        nombre: document.getElementById('nombreCliente').value.trim(),
        notas: document.getElementById('notasCliente').value.trim(),
        source: 'inline'
      });
    });
  }

  // Handler for Modal Form
  const modalBookingForm = document.getElementById('modalBookingForm');
  if (modalBookingForm) {
    modalBookingForm.addEventListener('submit', (e) => {
      e.preventDefault();
      sendQuoteToWhatsApp({
        fecha: document.getElementById('modalFechaEvento').value,
        tipo: document.getElementById('modalTipoEvento').value,
        personas: document.getElementById('modalCantidadPersonas').value,
        nombre: document.getElementById('modalNombreCliente').value.trim(),
        notas: document.getElementById('modalNotasCliente').value.trim(),
        source: 'modal'
      });
    });
  }

  // Escape key closes any active modal
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeQuoteModal();
      if (imageModal && imageModal.classList.contains('active')) {
        imageModal.classList.remove('active');
        imageModal.setAttribute('aria-hidden', 'true');
      }
    }
  });

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
