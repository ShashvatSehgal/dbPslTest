document.addEventListener('DOMContentLoaded', function() {
            M.toast({
                html: '{{ request.session.alert_message }}',
                classes: "{% if request.session.alert_type == 'success' %}green darken-1{% else %}red darken-1{% endif %} white-text",
                displayLength: 4000
            });
        });