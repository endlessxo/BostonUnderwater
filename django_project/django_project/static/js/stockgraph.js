var startdate = '2000-01-01';
var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1; //January is 0!
var yyyy = today.getFullYear();
 
today = yyyy + '-' + mm + '-' + dd;
 
$(document).ready(function(){ 
data = [{"date": "2015-02-07", "val": 1}, {"date":"2015-03-31", 3},{"date": "2015-03-31","val": 4}];
//drawGraph(data)
$.ajax({
    url: 'http://www.bostonunderwater.me/bostonunderwater/nodedata/',
    type: 'get', //this is the default though, you don't actually need to always mention it
    dataType: 'json',
    success: function(data) {
   
        alert('Good');
	alert(JSON.stringify(data));
        //chartData = JSON.stringify(data);
        drawGraph(data);
    },
    failure: function(data) {
        alert('Got an error dude');
    }
  });
});
 
function drawGraph(data) {
 
    chartdata = data;
    AmCharts.makeChart("chartdiv", {
    type: "stock",
    pathToImages: "/static/amstockchart_3.13.3.free/amcharts/images/",
    dataDateFormat: "YYYY-MM-DD",
    dataSets: [{
        dataProvider: chartdata,
        fieldMappings: [{
            fromField: "val",
            toField: "value"
        }],
        categoryField: "date"
    }],
 
    panels: [{
 
        legend: {},
 
        stockGraphs: [{
            id: "graph1",
            valueField: "value",
            type: "line",
            title: "",
            fillAlphas: 0,
            lineThickness: 3
        }]
    }],
 
    panelsSettings: {
        startDuration: 1
    },
 
    categoryAxesSettings: {
        dashLength: 5
    },
 
    valueAxesSettings: {
        dashLength: 5
    },
 
    chartScrollbarSettings: {
        graph: "graph1",
        graphType: "line"
    },
 
    chartCursorSettings: {
        valueBalloonsEnabled: true
    },
 
    periodSelector: {
        periods: [{
            period: "DD",
            count: 1,
            label: "1 day"
        }, {
            period: "DD",
            selected: true,
            count: 5,
            label: "5 days"
        }, {
            period: "MM",
            count: 1,
            label: "1 month"
        }, {
            period: "YYYY",
            count: 1,
            label: "1 year"
        }, {
            period: "YTD",
            label: "YTD"
        }, {
            period: "MAX",
            label: "MAX"
        }]
    }
});
}
