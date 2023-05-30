document.addEventListener("DOMContentLoaded", function () {
  const searchBox = document.querySelector("#search-box");
  const selectOrder = document.querySelector("#select-order");

  if (searchBox) {
    searchBox.addEventListener("input", function () {
      const searchText = searchBox.value;

      axios
        .get("/item/", {
          params: {
            search_filter: searchText,
          },
        })
        .then(function (response) {
          var newHtml = response.data.data.map(function (d) {
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
        .catch(function (error) {
          // TODO: show toaster
          console.log(error);
        });
    });
  }

  if (selectOrder) {
    selectOrder.addEventListener("change", function () {
      const selectedValue = selectOrder.value;
      console.log(selectedValue);

      axios
        .get("/item/", {
          params: {
            order_by: selectedValue,
          },
        })
        .then(function (response) {
          var newHtml = response.data.data.map(function (d) {
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
        .catch(function (error) {
          // TODO: show toaster
          console.log(error);
        });
    });
  }
});
