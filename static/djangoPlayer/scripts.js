document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('randomEpisode').addEventListener('click', function() {
    var totalEpisodesElement = document.getElementById('totalEpisodes');
    var stringValue = totalEpisodesElement.value;                           // get whole big string

    stringValue = stringValue.replace(/[\[\] ]/g, '');
    var availableEpisodes = stringValue.split(',');                         // convert this string to list of episodes

    var randomIndex = Math.floor(Math.random() * availableEpisodes.length); // get random episode
    var randomEpisodeNumber = availableEpisodes[randomIndex];

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
    var addToQueueButtons = document.querySelectorAll('.add-to-queue-btn');
    addToQueueButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var episodePK = this.getAttribute('data-pk');

            // Pobierz CSRF Token z metatagu
            var csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

            // Wyślij request AJAX
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/player/add_to_queue/', true);
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.setRequestHeader('X-CSRFToken', csrfToken);  // Dodaj ten nagłówek
            xhr.onload = function () {
                if (xhr.status === 200) {
                    var response = JSON.parse(xhr.responseText);
                    if (response.success) {
                        console.log('PK zapisane');
                    } else {
                        console.error(response.message);
                    }
                }
            };
            xhr.send('episode_pk=' + episodePK);
        });
    });
});

// document.addEventListener('DOMContentLoaded', function () {
//     // Pobierz listę odcinków z Local Storage
//     var episodesQueue = JSON.parse(localStorage.getItem('episodesQueue')) || [];
//     var listaKolejki = document.getElementById('lista-kolejki');
//     var hiddenInput = document.getElementById('base-lista-kolejki');
//     var buttons = document.querySelectorAll('.add-to-list');
//
//     function aktualizujWartoscInputa() {
//         hiddenInput.value = JSON.stringify(episodesQueue);
//     }
//
//     buttons.forEach(function (button) {
//         button.addEventListener('click', function () {
//             var episodeId = button.getAttribute('episode-pk');
//             episodesQueue.push(episodeId);
//
//             console.log('Queue of episodes:', episodesQueue);
//             console.log('Added episode: ' + episodeId);
//
//             // Po dodaniu odcinka do kolejki, zapisz zaktualizowaną listę w Local Storage
//             localStorage.setItem('episodesQueue', JSON.stringify(episodesQueue));
//
//             // Wyświetl zaktualizowaną listę na stronie
//             wyswietlListeKolejki();
//         });
//     });
//
//     function wyswietlListeKolejki() {
//         listaKolejki.innerHTML = '';
//
//         // Iteruj przez elementy kolejki i dodaj je do listy
//         episodesQueue.forEach(function (episodeId) {
//             var listItem = document.createElement('li');
//             listItem.textContent = 'Odcinek ' + episodeId;
//             listaKolejki.appendChild(listItem);
//
//             // Ustaw timer na 3000 milisekund (3 sekundy), aby usunąć element z listy
//             setTimeout(function () {
//                 listaKolejki.removeChild(listItem);
//             }, 3000);
//         });
//     }
//     aktualizujWartoscInputa()
// });


// document.addEventListener('DOMContentLoaded', function () {
//     var videoPlayer = document.getElementById('player');
//
//     var currentEpisodeNumber = window.location.pathname.split('/').slice(-2,-1)[0];
//     // Przekieruj użytkownika do następnego odcinka
//
//     var nextEpisodeNumber = parseInt(currentEpisodeNumber) + 1;
//     console.log(currentEpisodeNumber, nextEpisodeNumber)
//     // window.location.href = '{% url "player:video_detail" %}' + nextEpisodeNumber + '/';
//     // videoPlayer.addEventListener('ended', function () {
//     //     // Pobierz aktualny numer odcinka z URL
//     //     var currentEpisodeNumber = window.location.pathname.split('/').pop();
//     //     console.log(currentEpisodeNumber)
//     //
//     //     // Przekieruj użytkownika do następnego odcinka
//     //     var nextEpisodeNumber = parseInt(currentEpisodeNumber) + 1;
//     //     window.location.href = '{% url "player:odtwarzaj_odcinek" %}' + nextEpisodeNumber + '/';
//     // });
// });