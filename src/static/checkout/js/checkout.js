const handleSale = async (item) => {
  const offerId = item.id.toString().split("-")[2];
  try {
    const res = await axios.post(
      `/checkout/review`,
      {
        offerId: offerId,
      },
      {
        headers: {
          // HACK: Django throws 403 without this explicit csrf header
          "X-CSRFToken": getCookie("csrftoken"),
          // HACK: Better than using multipart/form-data since this is not form
          //       This needed explicit configuration in view
          "content-type": "application/json",
        },
      }
    );
    if (res) window.location.replace("/checkout/thank-you");
  } catch (error) {
    console.error(error);
  }
};

const handleRating = async (offerId, rating) => {
  try {
    await axios.post(
      "/checkout/thank-you",
      {
        offerId: offerId,
        rating: rating,
      },
      {
        headers: {
          // HACK: Django throws 403 without this explicit csrf header
          "X-CSRFToken": getCookie("csrftoken"),
          // HACK: Better than using multipart/form-data since this is not form
          //       This needed explicit configuration in view
          "content-type": "application/json",
        },
      }
    );
  } catch (error) {}
};

const fullName = document.querySelector("#full_name");
const streetName = document.querySelector("#street_name");
const houseNumber = document.querySelector("#house_number");
const city = document.querySelector("#city");
const country = document.querySelector("#country");
const postalCode = document.querySelector("#postal_code");
const cardHolder = document.querySelector("#card_holder");
const cardNumber = document.querySelector("#id_creditcard");
const expirationDate = document.querySelector("#id_date");
const cvc = document.querySelector("#id_cvc");

if (window.location.pathname == "/checkout/contact-information") {
  if (window.sessionStorage.getItem("fullName")) {
    fullName.value = window.sessionStorage.getItem("fullName");
  }
  fullName.addEventListener("change", () => {
    window.sessionStorage.setItem("fullName", fullName.value);
  });

  if (window.sessionStorage.getItem("streetName")) {
    streetName.value = window.sessionStorage.getItem("streetName");
  }
  streetName.addEventListener("change", () => {
    window.sessionStorage.setItem("streetName", streetName.value);
  });

  if (window.sessionStorage.getItem("houseNumber")) {
    houseNumber.value = window.sessionStorage.getItem("houseNumber");
  }
  houseNumber.addEventListener("change", () => {
    window.sessionStorage.setItem("houseNumber", houseNumber.value);
  });

  if (window.sessionStorage.getItem("city")) {
    city.value = window.sessionStorage.getItem("city");
  }
  city.addEventListener("change", () => {
    window.sessionStorage.setItem("city", city.value);
  });

  if (window.sessionStorage.getItem("country")) {
    country.value = window.sessionStorage.getItem("country");
  }
  country.addEventListener("change", () => {
    window.sessionStorage.setItem("country", country.value);
  });

  if (window.sessionStorage.getItem("postalCode")) {
    postalCode.value = window.sessionStorage.getItem("postalCode");
  }
  postalCode.addEventListener("change", () => {
    window.sessionStorage.setItem("postalCode", postalCode.value);
  });
}

if (window.location.pathname == "/checkout/payment-information") {
  if (window.sessionStorage.getItem("cardHolder")) {
    cardHolder.value = window.sessionStorage.getItem("cardHolder");
  }
  cardHolder.addEventListener("change", () => {
    window.sessionStorage.setItem("cardHolder", cardHolder.value);
  });

  if (window.sessionStorage.getItem("cardNumber")) {
    cardNumber.value = window.sessionStorage.getItem("cardNumber");
  }
  cardNumber.addEventListener("change", () => {
    window.sessionStorage.setItem("cardNumber", cardNumber.value);
  });

  if (window.sessionStorage.getItem("expirationDate")) {
    expirationDate.value = window.sessionStorage.getItem("expirationDate");
  }
  expirationDate.addEventListener("change", () => {
    window.sessionStorage.setItem("expirationDate", expirationDate.value);
  });

  if (window.sessionStorage.getItem("cvc")) {
    cvc.value = window.sessionStorage.getItem("cvc");
  }
  cvc.addEventListener("change", () => {
    window.sessionStorage.setItem("cvc", cvc.value);
  });
}

if (window.location.pathname == "/checkout/review") {
  fullName.value = window.sessionStorage.getItem("fullName");

  streetName.value = window.sessionStorage.getItem("streetName");

  houseNumber.value = window.sessionStorage.getItem("houseNumber");

  city.value = window.sessionStorage.getItem("city");

  country.value = window.sessionStorage.getItem("country");

  postalCode.value = window.sessionStorage.getItem("postalCode");

  cardHolder.value = window.sessionStorage.getItem("cardHolder");

  cardNumber.value = window.sessionStorage.getItem("cardNumber");

  expirationDate.value = window.sessionStorage.getItem("expirationDate");

  cvc.value = window.sessionStorage.getItem("cvc");

  const sellingItems = document.querySelectorAll("[id^=selling-item-]");
  document.querySelector("#confirm_purchase").addEventListener("click", (e) => {
    e.preventDefault();
    if (
      fullName.value == "" ||
      streetName.value == "" ||
      houseNumber.value == "" ||
      city.value == "" ||
      country.value == "" ||
      postalCode.value == "" ||
      cardHolder.value == "" ||
      cardNumber.value == "" ||
      expirationDate.value == "" ||
      cvc.value == "" ||
      sellingItems.length == 0
    ) {
      alert("Please fill in all required fields");
    } else {
      window.sessionStorage.clear();
      let count = 0;
      sellingItems.forEach((item) => {
        handleSale(item);
        const url = document.querySelector(
          `#selling-image-${item.id.split("-")[2]}`
        ).src;
        const name = document.querySelector(
          `#selling-name-${item.id.split("-")[2]}`
        );
        const amount = document.querySelector(
          `#selling-amount-${item.id.split("-")[2]}`
        );
        window.sessionStorage.setItem(`name-${count}`, name.innerHTML);
        window.sessionStorage.setItem(`amount-${count}`, amount.innerHTML);
        window.sessionStorage.setItem(`image-${count}`, url);
        window.sessionStorage.setItem("count", count);
        window.sessionStorage.setItem(
          `offerId-${count}`,
          item.id.toString().split("-")[2]
        );
        count++;
      });
    }
    //window.location.replace(confirmPurchaseBtn.href)
  });
}

if (window.location.pathname == "/checkout/thank-you") {
  if (typeof sessionStorage["count"] === "undefined") {
    window.location.replace("/unauthorized");
  }
  const soldItemsWrapper = document.querySelector(".thank-you-sold-items");
  let count = 0;
  for (element in window.sessionStorage.getItem("count")) {
    soldItemsWrapper.innerHTML += `
    <div class="single-checkout-item-wrapper">
                <img src="${window.sessionStorage.getItem(`image-${count}`)}"
                     alt="item image"
                     width="100"
                     height="100" />
                <div class="checkout-item-details">
                    <b>${window.sessionStorage.getItem(`name-${count}`)}</b>
                    <span>${window.sessionStorage.getItem(
                      `amount-${count}`
                    )}</span>
                </div>
            </div>
            <div class="rating-wrapper">
                <b>Rate the seller?</b>
                <fieldset class="rating">
                <button class="btn rate-button">Rate</button>
                    <input type="radio" name="rating" value="5" id="rating-5" class="offer-${window.sessionStorage.getItem(
                      `offerId-${count}`
                    )}" />
                    <label for="rating-5">☆</label>
                    <input type="radio" name="rating" value="4" id="rating-4" class="offer-${window.sessionStorage.getItem(
                      `offerId-${count}`
                    )}" />
                    <label for="rating-4">☆</label>
                    <input type="radio" name="rating" value="3" id="rating-3" class="offer-${window.sessionStorage.getItem(
                      `offerId-${count}`
                    )}" />
                    <label for="rating-3">☆</label>
                    <input type="radio" name="rating" value="2" id="rating-2" class="offer-${window.sessionStorage.getItem(
                      `offerId-${count}`
                    )}" />
                    <label for="rating-2">☆</label>
                    <input type="radio" name="rating" value="1" id="rating-1" class="offer-${window.sessionStorage.getItem(
                      `offerId-${count}`
                    )}" />
                    <label for="rating-1">☆</label>
                </fieldset>
            </div>
            <hr>
            <hr>
    `;
    count++;
  }

  const rating = document.querySelector(".rating");
  const rateBtn = document.querySelector(".rate-button");
  rateBtn.addEventListener("click", () => {
    const checkedItem = document.querySelector('input[name="rating"]:checked');
    handleRating(
      checkedItem.className.split("-")[1],
      checkedItem.id.split("-")[1]
    );
    rateBtn.disabled = true;
    rating.disabled = true;
  });
}
