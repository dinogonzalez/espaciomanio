/* ==========================================================================
   Espacio Mañio - Interactive Script (Datos Oficiales)
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  const WHATSAPP_MAIN = '56929055258';

  // Set Minimum Date for Reservation to Today
  const dateInput = document.getElementById('fechaEvento');
  if (dateInput) {
    const today = new Date().toISOString().split('T')[0];
    dateInput.min = today;
  }

  // Scroll Navbar effect
  const navbar = document.querySelector('.navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });

  // Handle Reservation Form Submission -> WhatsApp
  const bookingForm = document.getElementById('bookingForm');
  if (bookingForm) {
    bookingForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const fecha = document.getElementById('fechaEvento').value;
      const tipo = document.getElementById('tipoEvento').value;
      const personas = document.getElementById('cantidadPersonas').value;
      const nombre = document.getElementById('nombreCliente').value;
      const notas = document.getElementById('notasCliente').value;

      if (!fecha) {
        alert('Por favor selecciona una fecha para consultar disponibilidad.');
        return;
      }

      // Format Date nicely
      const dateParts = fecha.split('-');
      const dateFormatted = `${dateParts[2]}/${dateParts[1]}/${dateParts[0]}`;

      let message = `Hola *Espacio Mañio* 👋🏻, quisiera consultar valores y fechas para un evento:\n\n`;
      message += `📅 *Fecha del evento*: ${dateFormatted}\n`;
      message += `🎉 *Tipo de evento*: ${tipo}\n`;
      message += `👥 *Cantidad de asistentes*: ${personas}\n`;
      if (nombre) message += `👤 *Nombre*: ${nombre}\n`;
      if (notas) message += `📝 *Comentarios*: ${notas}\n`;
      message += `\n📍 *Ubicación*: Lonquén Sur, Paradero 38 1/2, Talagante\n`;
      message += `\nQuedo atento a su respuesta. ¡Muchas gracias!`;

      const encodedMessage = encodeURIComponent(message);
      const whatsappUrl = `https://wa.me/${WHATSAPP_MAIN}?text=${encodedMessage}`;

      window.open(whatsappUrl, '_blank');
    });
  }
});
