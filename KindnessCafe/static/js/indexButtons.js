function indexButtons() {
    // Log in & Sign up buttons
    $(".login-btn").modalForm({ formURL: "{% url 'login' %}" });
    $(".signup-btn").modalForm({ formURL: "{% url 'signup' %}" });
}