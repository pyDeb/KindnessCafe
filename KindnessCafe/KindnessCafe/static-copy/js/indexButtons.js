    // Log in & Sign up buttons
   // $(".login-btn").modalForm({ formURL: "{% url 'login' %}" });
   $(".signup-btn").click(function($)
   {
    $(".signup-btn").modalForm({ formURL: "{% url 'signup' %}" });
   });
   
    
