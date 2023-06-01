let params = {};

const handleClick = async (btn, status) => {
  // NOTE: Extracting ids from btn.id
  offerId = btn.id.toString().split("-")[2];
  itemId = btn.id.toString().split("-")[3];
  try {
    const res = await axios.post(
      `/item/see-offers/${itemId}`,
      {
        offerId: offerId,
        status: status,
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
    // NOTE: Redirecting to base.html
    if (res) window.location.replace("/");
  } catch (error) {
    console.log(error);
  }
};

// NOTE: Refactored from searchBox and selectOrder eventListeners
const getFiltered = async () => {
  try {
    const res = await axios.get("/item/", {
      // HACK: Using global variable as params
      params: params,
    });
    if (res) {
      var newHtml = res.data.data.map(function(d) {
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
    }
  } catch (error) {
    // TODO: show toaster
    console.error(error);
  }
};

document.addEventListener("DOMContentLoaded", function() {
  const searchBox = document.querySelector("#search-box");
  const selectOrder = document.querySelector("#select-order");
  const fileUpload = document.querySelector("#file-upload");
  const acceptBtns = document.querySelectorAll("[id^=accept-btn-]");
  const declineBtns = document.querySelectorAll("[id^=decline-btn-]");
  const createItemBtn = document.querySelector("#create-item-submit");

  if (searchBox) {
    searchBox.addEventListener("input", () => {
      // HACK: Update global variable
      params["search_filter"] = searchBox.value;
      getFiltered();
    });
  }

  if (selectOrder) {
    selectOrder.addEventListener("change", () => {
      // HACK: Update global variable
      params["order_by"] = selectOrder.value;
      getFiltered();
    });
  }

  if (createItemBtn) {
    // NOTE: Definition of createItemBtn implies existence of fileUpload
    createItemBtn.addEventListener("click", (e) => {
      if (fileUpload.validity.valueMissing) {
        alert("Please provide at least one image");
        e.preventDefault();
      } else if (fileUpload.validity.typeMismatch) {
        alert("Please provide only image files");
        e.preventDefault();
      }
    });
  }

  if (fileUpload) {
    fileUpload.addEventListener("change", (e) => {
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
