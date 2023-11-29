// everything should keep inside document.ready(), function run after html finish
$(document).ready(function(){
    var array = [];
    var heightWindow = $(window).height();
    var widthWindow = $(window).width();
// create 40 nodes
    for(var i = 0; i < 40; i++){
        array.push({
            //random coordinate of nodes in screen fram
            top: Math.floor(Math.random()*heightWindow),
            left: Math.floor(Math.random()*widthWindow),
            id: i
        })
    }
    array.forEach(function(value){
        var nodesVal = document.createElementNS('http://www.w3.org/2000/svg','ellipse');
        //gan thuoc tinh de co the xuat hien tren man hinh
        nodesVal.setAttribute('class','ellipse');
        nodesVal.setAttribute('id','ellipse_'+value.id);
        nodesVal.setAttribute('cx',value.left);  //x
        nodesVal.setAttribute('cy',value.top);   //y
        nodesVal.setAttribute('rx',5);           //radius
        nodesVal.setAttribute('ry',5);

        //append to id svg in html
        $('#svg').append(nodesVal);
        
    })

    $(window).mousemove(function(event){
         //remove old line of hover
         $('line').remove();
        (array.filter(val => Math.abs(val.top - event.pageY) <= 350 && Math.abs(val.left - event.pageX) <= 350)).forEach(function(value){
            var edgeVal = document.createElementNS('http://www.w3.org/2000/svg','line');
            //Gan thuoc tinh
            edgeVal.setAttribute('class','line');
            edgeVal.setAttribute('id','line_'+value.id);
            edgeVal.setAttribute('x1',value.left);  //x1 and node left
            edgeVal.setAttribute('y1',value.top);   //y1 and node top
            edgeVal.setAttribute('x2',event.pageX); //vi tri hien tai
            edgeVal.setAttribute('y2',event.pageY);
            //phai co stroke va mau, neu khong se k hien len
            edgeVal.setAttribute('stroke','black');
        
            //append to svg
            $('#svg').append(edgeVal);
        })
    })

    $(window).mouseout(function(event){
        //remove all lines when mouse out
        $('line').remove();
    })

    //Thay doi vi tri dau cham
    setInterval(function(){
        //Math.random()*(max-min)+min
        array.forEach(function(value,key){
            var top = Math.random()*((value.top + 5) - (value.top - 5)) + (value.top - 5);
            var left = Math.random()*((value.left + 5) - (value.left - 5)) + (value.left - 5);
            //gan vao array
            array[key].top = top;
            array[key].left = left;

            var $ellipse = $('#ellipse_' + value.id)
            $ellipse.animate({dot : 0},{
                step: () => {$ellipse.attr('cx',left),$ellipse.attr('cy',top)},
                duration: 1
            });
        })
    },500)
    console.log(array);
})

