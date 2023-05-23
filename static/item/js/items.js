$(document).ready(function () {
  $("#search-btn").on("click", function (e) {
    e.preventDefault();
    const searchText = $("#search-box").val();
    $.ajax({
      url: "/items?search_filter=" + searchText,
      type: "GET",
      success: function (resp) {
        const newHtml = resp.data.map((d) => {
          return `
            <div class="well candy">
              <a href="/item/${d.id}">
                <img class="item-img"
                  src="${d.firstImage}"
                  alt="item image"
                  width="100"
                  height="100" />
                  <h4>${d.name}</h4>
                <p>${d.description}</p>
              </a>
            </div>`;
        });
        $(".candies").html(newHtml.join(""));
        $("#search-box").val("");
      },
      error: function (xhr, status, error) {
        // TODO: show toaster
        console.log(error);
      },
    });
  });
});

const searchBtn = document.getElementById("#search-btn");
const searchText = document.getElementById("#search-box");

searchBtn.addEventListener(click, (e) => {
  e.preventDefault();
});
