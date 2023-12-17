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
    const bodyContent = document.querySelector("body::before");

    openSidebarButton.addEventListener("click", function () {
        sidebar.classList.toggle("show-sidebar");
        const isSidebarOpen = sidebar.classList.contains('show-sidebar');

        // Dostosuj padding-right w zależności od tego, czy boczny pasek nawigacyjny jest otwarty czy zamknięty
        headerContent.style.paddingRight = isSidebarOpen ? '430px' : '40px';
        mainContent.style.paddingRight = isSidebarOpen ? '430px' : '0';
        document.body.classList.toggle('overlay-active', isSidebarOpen);
    });
});
