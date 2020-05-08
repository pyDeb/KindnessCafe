    // Log in & Sign up buttons
   // $(".login-btn").modalForm({ formURL: "{% url 'login' %}" });
   $(".signup-btn").click(function($)
   {
    $(".signup-btn").modalForm({ formURL: "{% url 'signup' %}" });
   });
   $(document).ready(function(){
    var date_input=$('input[name="date"]'); //our date input has the name "date"
    var container=$('.bootstrap-iso form').length>0 ? $('.bootstrap-iso form').parent() : "body";
    var options={
      format: 'mm/dd/yyyy',
      container: container,
      todayHighlight: true,
      autoclose: true,
    };
    date_input.datepicker(options);
  })
    
