export const modalInit = () => {
  const modal = document.querySelector('[data-target="modal"]');
  const modalBg = document.querySelector('[data-target="modal-bg"]');
  const body = document.querySelector('body');

  const that = this;
  if (!modal) {
    return;
  }

  const trigger = document.querySelector('[data-target="modal-trigger"]');

  trigger.addEventListener('click', function(event) {
    event.preventDefault();
    modal.classList.add('open');
    body.classList.add('modal-open');
    const closeBtn = document.querySelector('[data-target="modal-close"]');

    const close = (event) => {
      event.preventDefault();
      modal.classList.remove('open');
      body.classList.remove('modal-open');
      event.target.removeEventListener('click', close);
      document.removeEventListener('keydown', close);
      modalBg.removeEventListener('click', close);
    };
    // bg.addEventListener('click', close(modal, event));
    closeBtn.addEventListener('click', function(event) {
      close(event);
    });

    document.addEventListener('keydown', function(event) {
      if (event.key === "Escape") {
        close(event);
      }
    });

    modalBg.addEventListener('click', function(event) {
      if (event.target !== modal) {
        close(event);
      }
    });
  });
};
