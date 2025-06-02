window.addEventListener('load', function () {
        const visitedFromBack = sessionStorage.getItem('visitedFromBack');

        // If already visited and coming again (back button)
        if (visitedFromBack === 'true') {
            console.log('Back navigation detected. Reloading...');
            sessionStorage.removeItem('visitedFromBack'); // optional cleanup
            location.reload(); // force reload on back nav
        } else {
            sessionStorage.setItem('visitedFromBack', 'true');
        }

        // Optional: Reset session flag on leaving
        window.addEventListener('beforeunload', function () {
            sessionStorage.removeItem('visitedFromBack');
        });
    });