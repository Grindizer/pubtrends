$( document ).ready(function() {
    function draw_bar(data, container, key, value) {
        var margin = {top: 20, right: 20, bottom: 30, left: 60},
            width = $(container).width() - margin.left - margin.right,
            height = $(container).height() - margin.top - margin.bottom

        //var barWidth = Math.floor(width / keys.length) - 1;
        var barWidth = 30;
        var x = d3.scale.ordinal()
            .domain(data.map(function (d) { return key(d)} ))
            .rangeRoundBands([0, width], .1);
            //.range([0, width]);

        var y = d3.scale.linear()
            .domain([0, d3.max(data, function(d) { return value(d); })])
            .range([height, 0]);

        var xAxis = d3.svg.axis()
            .scale(x)
            .orient("bottom");

        var yAxis = d3.svg.axis()
            .scale(y)
            .orient("left")
            .ticks(10);


        //debugger;
        $(container).html("");
        var svg = d3.select(container).append("svg")
                    .attr("width", width + margin.left + margin.right)
                    .attr("height", height + margin.top + margin.bottom)
                .append("g")
                    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        svg.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(xAxis);

        svg.append("g")
            .attr("class", "y axis")
            .call(yAxis)
           .append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "end")
            .text("count");

        svg.selectAll(".bar")
            .data(data)
          .enter().append("rect")
            .attr("class", "bar")
            .attr("x", function(d) { return x(key(d)); })
            .attr("width", x.rangeBand())
            .attr("y", function(d) { return y(value(d)); })
            .attr("height", function(d) { return height - y(value(d)); })
          .append("title").text(function(d) { return value(d); });
        //$("#per_year_chart").show();

    };
    // submit data when click button.
    $("#go").click(function (){
        var data = {
            start: $("#start input").val(), //'2010',
            stop: $("#stop input").val(),
            term: $("#term input").val()
        };
        $("#map").replaceWith("<div id='map'></div>").css('visibility', 'hidden');

        $("#map").css('visibility', 'hidden');
        $("#per_year_chart").css('visibility', 'hidden');
        $(".maps").css('visibility', 'hidden');
        $.ajax({
            url: "/api/per_year/",
            data: data,
            dataType: 'json',
            success: function(data) {
                //update_per_year_graph(data, "#per_year_chart");
                $("#per_year_chart").css('visibility', 'visible');
                draw_bar(data, "#per_year_chart",
                    function (d) {
                        return d.year
                    },
                    function (d) {
                        return d.count
                    });
                $(".maps").css('visibility', 'visible');
            }
        });
        $.ajax({
            url: "/api/locations/",
            data: data,
            dataType: 'json',
            success: function(data) {
                $(".loading").css('visibility', 'hidden');
                $("#map").css('visibility', 'visible');
                draw_map(data, "map",
                    function (d) {
                        return d.country
                    },
                    function (d) {
                        return d.count
                    });
            }
        });

    });



})