$(document).ready(function () {
  $("#search-btn").on("click", function (e) {
    e.preventDefault();
    var searchText = $("#search-box").val();
    $.ajax({
      url: "/item/?search_filter=" + searchText,
      type: "GET",
      success: function (resp) {
        console.log(resp.data);
        var newHtml = resp.data.map((d) => {
          return `<div class="well item">
                    <a href="/item/${d.id}">
                      <img class="item-img" src="${d.firstImage}" />
                      <h4>${d.name}</h4>
                      <p>${d.description}</p>
                    </a>
                  </div>`;
        });
        $(".item").html(newHtml.join(""));
        $("#search-box").val("");
      },
      error: function (xhr, status, error) {
        // TODO: show toaster
        console.log(error);
      },
    });
  });
});
