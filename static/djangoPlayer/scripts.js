document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('randomEpisode').addEventListener('click', function() {
    let totalEpisodesElement = document.getElementById('totalEpisodes');
    let stringValue = totalEpisodesElement.value;                           // get whole big string

    stringValue = stringValue.replace(/[\[\] ]/g, '');
    let availableEpisodes = stringValue.split(',');                         // convert this string to list of episodes

    let randomIndex = Math.floor(Math.random() * availableEpisodes.length); // get random episode
    let randomEpisodeNumber = availableEpisodes[randomIndex];

    window.location.href = '/player/video/' + randomEpisodeNumber + '/';    // go to page
    });
});
document.addEventListener("DOMContentLoaded", function () {
    const openSidebarButton = document.getElementById("openSidebarButton");
    const sidebar = document.querySelector(".sidebar");
    const headerContent = document.querySelector(".header-content");
    const mainContent = document.querySelector(".main");

    openSidebarButton.addEventListener("click", function () {
        sidebar.classList.toggle("show-sidebar");
        const isSidebarOpen = sidebar.classList.contains('show-sidebar');

        // Dostosuj padding-right w zależności od tego, czy boczny pasek nawigacyjny jest otwarty czy zamknięty
        headerContent.style.paddingRight = isSidebarOpen ? '430px' : '40px';
        mainContent.style.paddingRight = isSidebarOpen ? '430px' : '0';
        document.body.classList.toggle('overlay-active', isSidebarOpen);
    });
});

document.addEventListener('DOMContentLoaded', function () {
    let addToQueueButtons = document.querySelectorAll('.add-to-queue-btn');
    addToQueueButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            let episodePK = this.getAttribute('data-pk');

            // Pobierz CSRF Token z metatagu
            let csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

            // Wyślij request AJAX
            let xhr = new XMLHttpRequest();
            xhr.open('POST', '/player/add_to_queue/', true);
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.setRequestHeader('X-CSRFToken', csrfToken);  // Dodaj ten nagłówek
            xhr.onload = function () {
                if (xhr.status === 200) {
                    let response = JSON.parse(xhr.responseText);
                    if (response.success) {
                        console.log('episode saved');
                        // Wymuś przeładowanie strony
                        location.reload();
                    } else {
                        console.error(response.message);
                    }
                }
            };
            xhr.send('episode_pk=' + episodePK);
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {

    let addToQueueButtons = document.querySelectorAll('.add-to-queue-btn');
    addToQueueButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            button.classList.add('saved');
        });
    });
});

