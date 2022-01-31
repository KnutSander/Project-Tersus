Chart.defaults.line.spanGaps = true;
var data = {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
    datasets: [{
      label: "Dataset #1",
      backgroundColor: "rgba(255,99,132,0.2)",
      borderColor: "rgba(255,99,20,1)",
      borderWidth: 2,
      hoverBackgroundColor: "rgba(255,99,132,0.4)",
      hoverBorderColor: "rgba(255,9,132,1)",
      data: [65, 59, 24, 81, 56, 55, 40],
    }]
  };
  var data2= {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 29, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    };
  
  var Baroptions = {
    maintainAspectRatio: false,
    responsive: true,
    animation: {
        duration: 5000 // general animation time
    },
    scales: {
      yAxes: [{
        stacked: false,
        gridLines: {
          display: true,
          color: "rgba(255,99,132,0.2)"
        }
      }],
      xAxes: [{
        gridLines: {
          display: false
        }
      }]
    }
  };


  Chart.Bar('myChart',{
options:Baroptions,
data:data2
  });

  Chart.Bar('chart', {
    options: Baroptions,
    data: data
  });