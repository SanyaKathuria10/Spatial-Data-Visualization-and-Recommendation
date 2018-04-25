d3.csv("data/top_categories.csv", function(error, data) {
  var no_Of_checkins = d3.nest()
    .key(function(d){ return d.Venue; })
    .map(data);
  var top_categories = d3.nest()
    .key(function(d){ return d.Category; })
    .map(data); 
  var fig_width=1000, fig_height=625;
  var fig = d3.select("#category-chart")
    .append('fig')
    .attr("viewBox", "0 0 " + fig_width + " " + fig_height)
    .style("max-width", fig_width + "px")
    .attr("preserveAspectRatio", "xMidYMid meet");
  var hist = fig.append("g")
  .attr('transform', "translate(" + margin.left + ", " + margin.top + ")");
  var hist_width = fig_width - (margin.left + margin.right),
      hist_height = fig_height - (margin.top + margin.bottom);
  var x_max = 10;
  var y_scale = d3.scale.ordinal()
                .rangeBands([0, hist_height], 0.2, 0.2),
      x_scale = d3.scale.linear()
                .domain([0, x_max])
                .range([0, hist_width]),
      color_scale = d3.scale.category20().domain(Object.keys(top_categories));
  var x_axis = d3.fig.axis().scale(x_scale).orient('bottom').tickFormat(function(d) { return d+"%"; }),
      y_axis = d3.fig.axis().scale(y_scale).orient('left');

  function updateHist (no_Of_checkins, venue) {
    var catg_list = [];
    catg_list.length = 0;
    k = 0
    while (k<12) {
      catg_list.push({
        key: no_Of_checkins[venue][k].Category,
        value: no_Of_checkins[venue][k].Percentage
      });
      k++;
    }
    
    var category_key_list = [];
    category_key_list = catg_list.map(function(d) { return d.key; });
    x_max = d3.max(no_Of_checkins[venue], function(d){ return +d['Percentage']; })
    
    x_scale.domain([0, x_max*1.20]);
    y_scale.domain(category_key_list);

    hist.select('#x-axis').transition().call(x_axis)
    hist.select('#y-axis').transition().call(y_axis)

    var figure = hist.selectAll('rect')
      .data(catg_list);

    figure
      .enter()
      .append('rect')
      .attr('height', y_scale.rangeBand());

    figure
      .attr('y', function(d) {
        return y_scale(d.key);
      })
      .attr('x', 1)
      .style('fill', function(d){
        return color_scale(d.key);
      })
      .style('opacity', 0.40)
      .transition()
      .attr('width', function(d){
        return x_scale(d.value);
      });
    figure.exit().remove();
    var labels = hist.selectAll("text")
      .data(catg_list, function(d) { return d.key; });
	  
    labels.enter()
      .append('text')
      .text(function(d) {
        return d.key;
      })
      .attr('y', function(d, i) {
        return y_scale(d.key) + y_scale.rangeBand();
      })
      .attr('x', function (d) {
        return x_scale(d.value) + 10;
      })
      .attr('class', 'venue-label')
      .style('text-anchor', 'begin');

    labels
      .attr('y', function(d, i) {
        return y_scale(d.key) + y_scale.rangeBand() -10;
      })
      .attr('x', function (d) {
        return x_scale(d.value) + 7;
    });
  }
  var margin = {
    'top': 5,
    'right': 5,
    'bottom': 10,
    'left': 10
  };

  hist.append('g')
    .attr('class', 'axis')
    .attr('id', 'x-axis')
    .call(x_axis)
    .attr('transform', 'translate(0, ' + hist_height + ')');
  hist.append('g')
    .attr('class', 'axis')
    .call(y_axis);
	
  updateHist(no_Of_checkins, "Manhattan")
  $(document).ready(function() {
    $('.btn-venue').click(function() {
      var venue = $(this).attr('value');
      $(".venue-label").remove();
      updateHist(no_Of_checkins, venue);
    })
  })
})