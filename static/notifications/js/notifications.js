const handleNotification = (btn) => {
  // NOTE: Send empty post request to notifications/:id to update read status
  const notificationId = btn.id.toString().split("-")[2];
  axios
    .post(
      `/notifications/${notificationId}`,
      {},
      {
        headers: {
          // HACK: Django throws 403 without this explicit csrf header
          "X-CSRFToken": getCookie("csrftoken"),
          // HACK: Better than using multipart/form-data since this is not form
          //       This needed explicit configuration in view
          "content-type": "application/json",
        },
      }
    )
    .then((res) => {
      console.log(res.data);
    })
    .catch((e) => {
      console.error(e);
    });
};

document.addEventListener("DOMContentLoaded", function() {
  const notificationBtns = document.querySelectorAll("[id^=notification-btn-]");

  if (notificationBtns) {
    notificationBtns.forEach((btn) => {
      btn.addEventListener("click", (e) => {
        e.preventDefault()
        handleNotification(btn);
      });
    });
  }
});
