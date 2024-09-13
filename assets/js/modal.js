

export const modalInit = () => {
  const modal = document.querySelector('[data-target="modal"]');
  const body = document.querySelector('body');


  // console.log(modal);
  if (!modal) {
    return;
  }

  const trigger = document.querySelector('[data-target="modal-trigger"]');
  // const bg = document.querySelector('[data-target="modal-bg"]');

  console.log(trigger);
  trigger.addEventListener('click', function(event) {
    event.preventDefault();
    console.log(modal);
    modal.classList.add('open');
    body.classList.add('modal-open');

    const closeBtn = document.querySelector('[data-target="modal-close"]');

    const close = (event) => {
      event.preventDefault();
      modal.classList.remove('open');
      body.classList.remove('modal-open');
      event.target.removeEventListener('click', close);
      document.removeEventListener('keydown', close);
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

  });
};
