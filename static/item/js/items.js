document.addEventListener("DOMContentLoaded", function() {
  const searchBox = document.querySelector("#search-box");
  const selectOrder = document.querySelector("#select-order");
  const fileUpload = document.querySelector("#file-upload");
  const acceptBtns = document.querySelectorAll("[id^=accept-btn-]");
  const declineBtns = document.querySelectorAll("[id^=decline-btn-]");

  if (searchBox) {
    searchBox.addEventListener("input", function() {
      const searchText = searchBox.value;

      axios
        .get("/item/", {
          params: {
            search_filter: searchText,
          },
        })
        .then(function(response) {
          var newHtml = response.data.data.map(function(d) {
            return `<a href="/item/${d.id}" class="single-item">
            <div class="image-container">
                <img class="item-img"
                     src="${d.firstImage}"
                     alt="item image"
                     width="300"
                     height="300" />
            </div>
            <h4>Name: ${d.name}</h4>
            <p>Price: ${d.price} kr</p>
            </a>`;
          });

          document.querySelector(".items-grid").innerHTML = newHtml.join("");
        })
        .catch(function(error) {
          // TODO: show toaster
          console.log(error);
        });
    });
  }

  if (selectOrder) {
    selectOrder.addEventListener("change", function() {
      const selectedValue = selectOrder.value;
      console.log(selectedValue);

      axios
        .get("/item/", {
          params: {
            order_by: selectedValue,
          },
        })
        .then(function(response) {
          var newHtml = response.data.data.map(function(d) {
            return `<a href="/item/${d.id}" class="single-item">
            <div class="image-container">
                <img class="item-img"
                     src="${d.firstImage}"
                     alt="item image"
                     width="300"
                     height="300" />
            </div>
            <h4>Name: ${d.name}</h4>
            <p>Price: ${d.price} kr</p>
            </a>`;
          });

          document.querySelector(".items-grid").innerHTML = newHtml.join("");
        })
        .catch(function(error) {
          // TODO: show toaster
          console.log(error);
        });
    });
  }

  if (fileUpload) {
    fileUpload.addEventListener("change", function(e) {
      const displayFiles = document.querySelector("#display-files");
      displayFiles.innerHTML = fileUpload.value.substring(12);
    });
  }

  if (declineBtns) {
    declineBtns.forEach((btn) => {
      btn.addEventListener("click", (e) => {
        e.preventDefault();
        handleClick(btn, "Declined");
      });
    });
  }

  if (acceptBtns) {
    acceptBtns.forEach((btn) => {
      btn.addEventListener("click", (e) => {
        e.preventDefault();
        handleClick(btn, "Accepted");
      });
    });
  }
});

const handleClick = (btn, status) => {
  // NOTE: Extracting ids from btn.id
  offerId = btn.id.toString().split("-")[2];
  itemId = btn.id.toString().split("-")[3];
  axios
    .post(
      `/item/see-offers/${itemId}`,
      {
        offerId: offerId,
        status: status,
      },
      {
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          "content-type": "application/json",
        },
      }
    )
    .then((res) => {
      window.location.replace("/");
    })
    .catch((e) => console.error(e));
};

const getCookie = (name) => {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    let cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      let cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
