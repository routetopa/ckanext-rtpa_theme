jQuery(document).ready(function () {

    jQuery('.tet_lang_dropdown_toggle').on('click', function (event) {
        // Avoid following the href location when clicking
        event.preventDefault();

        // Avoid having the menu to close when clicking
        event.stopPropagation();

        jQuery('.tet_language_popup').toggle();

    });

});