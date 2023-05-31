if (window.location.pathname == "/checkout/contact-information") {
  const fullName = document.querySelector("#full_name");
  if (window.sessionStorage.getItem("fullName")) {
    fullName.value = window.sessionStorage.getItem("fullName");
  }
  fullName.addEventListener("change", () => {
    window.sessionStorage.setItem("fullName", fullName.value);
  });

  const streetName = document.querySelector("#street_name");
  if (window.sessionStorage.getItem("streetName")) {
    streetName.value = window.sessionStorage.getItem("streetName");
  }
  streetName.addEventListener("change", () => {
    window.sessionStorage.setItem("streetName", streetName.value);
  });

  const houseNumber = document.querySelector("#house_number");
  if (window.sessionStorage.getItem("houseNumber")) {
    houseNumber.value = window.sessionStorage.getItem("houseNumber");
  }
  houseNumber.addEventListener("change", () => {
    window.sessionStorage.setItem("houseNumber", houseNumber.value);
  });

  const city = document.querySelector("#city");
  if (window.sessionStorage.getItem("city")) {
    city.value = window.sessionStorage.getItem("city");
  }
  city.addEventListener("change", () => {
    window.sessionStorage.setItem("city", city.value);
  });

  const country = document.querySelector("#country");
  if (window.sessionStorage.getItem("country")) {
    country.value = window.sessionStorage.getItem("country");
  }
  country.addEventListener("change", () => {
    window.sessionStorage.setItem("country", country.value);
  });

  const postalCode = document.querySelector("#postal_code");
  if (window.sessionStorage.getItem("postalCode")) {
    postalCode.value = window.sessionStorage.getItem("postalCode");
  }
  postalCode.addEventListener("change", () => {
    window.sessionStorage.setItem("postalCode", postalCode.value);
  });
}

if (window.location.pathname == "/checkout/payment-information") {
  const cardHolder = document.querySelector("#card_holder");
  if (window.sessionStorage.getItem("cardHolder")) {
    cardHolder.value = window.sessionStorage.getItem("cardHolder");
  }
  cardHolder.addEventListener("change", () => {
    window.sessionStorage.setItem("cardHolder", cardHolder.value);
  });

  const cardNumber = document.querySelector("#id_creditcard");
  if (window.sessionStorage.getItem("cardNumber")) {
    cardNumber.value = window.sessionStorage.getItem("cardNumber");
  }
  cardNumber.addEventListener("change", () => {
    window.sessionStorage.setItem("cardNumber", cardNumber.value);
  });

  const expirationDate = document.querySelector("#id_date");
  if (window.sessionStorage.getItem("expirationDate")) {
    expirationDate.value = window.sessionStorage.getItem("expirationDate");
  }
  expirationDate.addEventListener("change", () => {
    window.sessionStorage.setItem("expirationDate", expirationDate.value);
  });

  const cvc = document.querySelector("#id_cvc");
  if (window.sessionStorage.getItem("cvc")) {
    cvc.value = window.sessionStorage.getItem("cvc");
  }
  cvc.addEventListener("change", () => {
    window.sessionStorage.setItem("cvc", cvc.value);
  });
}

if (window.location.pathname == "/checkout/review") {
  document.querySelector("#full_name").value =
    window.sessionStorage.getItem("fullName");

  document.querySelector("#street_name").value =
    window.sessionStorage.getItem("streetName");

  document.querySelector("#house_number").value =
    window.sessionStorage.getItem("houseNumber");

  document.querySelector("#city").value = window.sessionStorage.getItem("city");

  document.querySelector("#country").value =
    window.sessionStorage.getItem("country");

  document.querySelector("#postal_code").value =
    window.sessionStorage.getItem("postalCode");

  document.querySelector("#card_holder").value =
    window.sessionStorage.getItem("cardHolder");

  document.querySelector("#card_number").value =
    window.sessionStorage.getItem("cardNumber");

  document.querySelector("#expiration_date").value =
    window.sessionStorage.getItem("expirationDate");

  document.querySelector("#cvc").value = window.sessionStorage.getItem("cvc");

  document.querySelector("#confirm_purchase").addEventListener("click", () => {
    window.sessionStorage.clear();
    // TODO: sell the item
  });
}
