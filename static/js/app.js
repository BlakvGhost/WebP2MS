((function () {

    "use strict"

    const $pathname = location.pathname;
    const $menuItems = document.querySelectorAll("#kt_app_sidebar_menu_wrapper .menu-link");

    $menuItems.forEach(($menuItem) => {
        const pathname = $pathname;

        if (pathname === $menuItem.getAttribute("data-web-link")) {
            $menuItem.classList.add("menu-active");
        }
    })
    // document.addEventListener('DOMContentLoaded', function () {
    //     const installBar = document.querySelector('.install-bar');
    //     const installButton = document.querySelector('.install-button');
    //     const refuseButton = document.querySelector('.refuse-button');

    //     let deferredPrompt;
    //     // Vérifier si la barre d'installation est présente dans le DOM
    //     // window.addEventListener('beforeinstallprompt', (event) => {
    //     //     event.preventDefault();
    //     //     deferredPrompt = event;
    //     //     // Afficher la barre d'installation ou exécuter une autre action pour inviter les utilisateurs à installer l'application
    //     //     showInstallPrompt();
    //     // });
    //     if (installBar) {
    //         // Vérifier si l'API d'installation est prise en charge
    //         if (true) {
    //             // Cacher la barre d'installation par défaut
    //             installBar.classList.remove('show');

    //             // Gestionnaire d'événement pour le bouton "Installer"
    //             installButton.addEventListener('click', function () {

    //                 const installData = {
    //                     // Mettez ici les informations nécessaires pour l'installation de votre PWA
    //                     // Par exemple, le nom de votre application, l'icône, etc.
    //                     name: 'Mon application',
    //                     icon: '/path/to/icon.png',
    //                     // ...
    //                 };

    //                 // Appeler la méthode `prompt` pour afficher la boîte de dialogue d'installation
    //                 window.navigator.install.prompt()
    //                     .then(function (choice) {
    //                         // Vérifier si l'utilisateur a installé ou annulé l'installation
    //                         if (choice.outcome === 'accepted') {
    //                             console.log('L\'application a été installée avec succès.');
    //                         } else {
    //                             console.log('L\'installation de l\'application a été annulée.');
    //                         }
    //                     })
    //                     .catch(function (error) {
    //                         console.error('Une erreur est survenue lors de l\'installation de l\'application:', error);
    //                     });
    //             });

    //             // Gestionnaire d'événement pour le bouton "Refuser"
    //             refuseButton.addEventListener('click', function () {
    //                 // Cacher la barre d'installation
    //                 installBar.classList.remove('show');
    //                 // Enregistrer le refus dans le stockage local
    //                 localStorage.setItem('installPromptRejected', true);
    //             });

    //             // Vérifier si la barre d'installation doit être affichée
    //             if (!localStorage.getItem('installPromptRejected') && !localStorage.getItem('installPromptShown')) {
    //                 // Afficher la barre d'installation après un certain délai (par exemple, 5 secondes)
    //                 setTimeout(function () {
    //                     installBar.classList.add('show');
    //                 }, 5000);

    //                 // Enregistrer l'affichage de la barre d'installation
    //                 localStorage.setItem('installPromptShown', true);

    //                 // Définir une expiration pour l'affichage de la barre d'installation (5 jours)
    //                 const expirationDate = new Date().getTime() + 5 * 24 * 60 * 60 * 1000;
    //                 localStorage.setItem('installPromptExpiration', expirationDate);
    //             } else {
    //                 // Vérifier si la période d'expiration est écoulée
    //                 const expirationDate = localStorage.getItem('installPromptExpiration');
    //                 if (expirationDate && new Date().getTime() > parseInt(expirationDate)) {
    //                     // Supprimer les données de l'affichage précédent
    //                     localStorage.removeItem('installPromptShown');
    //                     localStorage.removeItem('installPromptExpiration');
    //                 }
    //             }
    //         } else {
    //             console.warn('L\'API d\'installation n\'est pas prise en charge.');
    //         }
    //     }
    // });


})())