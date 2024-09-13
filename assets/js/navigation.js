export const navigation = () => {
  const navigationToggle = document.querySelector(
    '[data-target="navigation-toggle-button"]',
  );

  const navigationList = document.querySelector(
    '[data-target="navigation-toggle-list"]',
  );

  const toggleNavigation = () => {
    const isOpen = navigationToggle.classList.contains("is-open");
    navigationToggle.classList.replace(
      isOpen ? 'is-open' : 'is-closed',
      !isOpen ? 'is-open' : 'is-closed',
    );

    navigationList.classList.replace(
      isOpen ? 'is-open' : 'is-closed',
      !isOpen ? 'is-open' : 'is-closed',
    );
  };

  navigationToggle.addEventListener('click', toggleNavigation);
};
