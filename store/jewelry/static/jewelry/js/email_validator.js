(() => {

  const MESSAGES = {
    en: {
      required: "Please enter your email",
      invalid: "Invalid email format",
    },

  };
  const LANG = "en";
  const T = (k) => (MESSAGES[LANG] && MESSAGES[LANG][k]) || k;

  const FORM_SELECTORS = [
    'form[data-email-form]',
    '#checkout-form',
    '#contacts-form',
    'form.checkout',
    'form.contacts'
  ];

  const EMAIL_RE = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i;

  const forms = new Set();
  FORM_SELECTORS.forEach(sel =>
    document.querySelectorAll(sel).forEach(f => forms.add(f))
  );
  if (!forms.size) return;

  forms.forEach(form => {
    const emailInput =
      form.querySelector('[data-email-input]') ||
      form.querySelector('input[type="email"]');
    if (!emailInput) return;

    let errorEl =
      form.querySelector('[data-email-error]') || createErrorEl(emailInput);

    emailInput.addEventListener('input', validate);
    emailInput.addEventListener('blur', validate);
    form.addEventListener('submit', e => {
      if (!validate()) {
        e.preventDefault();
        emailInput.focus();
      }
    });

    function validate() {
      const value = (emailInput.value || '').trim();
      if (!value) {
        setError(T('required'));
        return false;
      }
      if (!EMAIL_RE.test(value)) {
        setError(T('invalid'));
        return false;
      }
      clearError();
      return true;
    }

    function setError(msg) {
      errorEl.textContent = msg;
      errorEl.hidden = false;
      emailInput.classList.add('is-invalid');
      emailInput.setAttribute('aria-invalid', 'true');
      emailInput.setAttribute('aria-describedby', errorEl.id);
    }

    function clearError() {
      errorEl.textContent = '';
      errorEl.hidden = true;
      emailInput.classList.remove('is-invalid');
      emailInput.removeAttribute('aria-invalid');
      emailInput.removeAttribute('aria-describedby');
    }

    function createErrorEl(afterEl) {
      const el = document.createElement('small');
      el.className = 'field-error';
      el.hidden = true;
      el.id = 'email-error-' + Math.random().toString(36).slice(2, 8);
      el.setAttribute('data-email-error', '');
      afterEl.insertAdjacentElement('afterend', el);
      return el;
    }
  });
})();
