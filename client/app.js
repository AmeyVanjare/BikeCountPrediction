function onClickedEstimatedCount() {
    console.log("Estimate price button clicked");
    var season = document.getElementById("season");
    var workingday = document.getElementById("workingday");
    var temp = document.getElementById("temp");
    var atemp = document.getElementById("atemp");
    var humidity = document.getElementById("humidity");
    var windspeed = document.getElementById("windspeed");
    var estCount = document.getElementById("uiEstimatedCount");
  
    var url = "http://127.0.0.1:5000/predict_casual_count"; 
   
    $.post(url, {
        season: season,
        workingday: workingday,
        temp: parseFloat(temp),
        atemp: parseFloat(atemp),
        humidity: parseFloat(humidity),
        windspeed: parseFloat(windspeed)
    },function(data, status) {
        console.log(data.estimated_count);
        estCount.innerHTML = "<h2>" + data.estimated_count.toString() + "</h2>";
        console.log(status);
    });
  }