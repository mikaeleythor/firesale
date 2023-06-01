const handleNotification = async (btn) => {
  // NOTE: Send empty post request to notifications/:id to update read status
  const notificationId = btn.id.toString().split("-")[2];
  try {
    const res = await axios.post(
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
    if (res) console.log(res.data);
  } catch (error) {
    console.error(error)
  }
};

document.addEventListener("DOMContentLoaded", function() {
  const notificationBtns = document.querySelectorAll("[id^=notification-btn-]");

  if (notificationBtns) {
    notificationBtns.forEach((btn) => {
      btn.addEventListener("click", async (e) => {
        e.preventDefault()
        await handleNotification(btn);
        window.location.replace(btn.href)
      });
    });
  }
});
