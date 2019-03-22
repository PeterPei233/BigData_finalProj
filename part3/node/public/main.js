$(function () {
	var data_points = [];
	data_points.push({values:[], key:'BTC-USD'});

	$('#chart').height($(window).height() - $('#header').height() * 2);

	var chart = nv.models.lineChart()
		.interpolate('monotone')
		.margin({
			bottom:100
		})
		.useInteractiveGuideline(true)
		.showLegend(true)
		.color(d3.scale.category10().range());

	chart.xAxis
		.axisLabel('Time')
		.tickFormat(formatDateTick);

	chart.yAxis
		.axisLabel('Price');


	nv.addGraph(loadGraph);

	function loadGraph() {
		d3.select('#chart svg')
			.datum(data_points)
			.transition()
			.duration(5)
			.call(chart)

		nv.utils.windowResize(chart.update);
		return chart;
	}

	function formatDateTick(time) {
		var date = new Date(time);
		console.log(time);
		return d3.time.format('%H:%M:%S')(date);
	}

	function newDataCallback(data) {
		var parsed = JSON.parse(data);
		var timestamp = parsed['Timestamp'];
		var average = parsed['Average'];
		var symbol = parsed['Symbol'];
		var point = {};
		point.x = timestamp;
		point.y = average;

		console.log(point);

		var i = _getSymbolIndex(symbol, data_points);
		data_points[i].values.push(point);
		if (data_points[i].values.length > 100) {
			data_points[i].values.shift();
		}
		loadGraph();
	}

	function _getSymbolIndex(symbol, array) {
		for (var i = 0; i < array.length; i++) {
			if (array[i].key == symbol) {
				return i;
			}
		}
		return -1;
	}

	var socket = io();

	// Whenever the server emits 'data', update the graph.
	socket.on('data', function(data) {
		newDataCallback(data);
	});
});

