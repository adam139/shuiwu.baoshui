/*jshint sub:true*/

function closeSearchEventsDiv(flag) {
    if (flag == 1) {
        $("#dateSearch").val("0");
        $("#dateRangeSearchUl li> .over a").removeClass("btn-primary").addClass("btn-default");
        $("#dateRangeSearchUl li> .over").removeClass("over");
        $("#dateRangeSearchUl").find("li span[data-name='0']").addClass("over");
        $("#dateRangeSearchUl li> .over a").removeClass("btn-default").addClass("btn-primary");
        searchEvent();
    } else if (flag == 2) {
        $("#annualSearch").val("0");
        $("#annualRangeSearchUl li> .over a").removeClass("btn-primary").addClass("btn-default");
        $("#annualRangeSearchUl li> .over").removeClass("over");
        $("#annualRangeSearchUl").find("li span[data-name='0']").addClass("over");
        $("#annualRangeSearchUl li> .over a").removeClass("btn-default").addClass("btn-primary");
        searchEvent();
    } else if (flag == 3) {
        $("#categorySearch").val("0");
        $("#categorySelectSearch li> .over").removeClass("over");
        $("#categorySelectSearch").find("li span[data-name='0']").addClass("over");
        searchEvent();
    }
    else if (flag == 4) {
        $("#tagSearch").val("0");
        $(".tagSelectSearch").each(function(){
        	$(this).find("li> .over a").removeClass("btn-primary").addClass("btn-default");
        	$(this).find("li> .over").removeClass("over");
        }); 
        $(".tagSelectSearch").each(function(){
    	$(this).find("li span[data-name='0']").addClass("over");
    	$(this).find("li span[data-name='0'] a").removeClass("btn-default").addClass("btn-primary");
    	$(this).find(".hidden input").val("0");});
        searchEvent();
    }    
}

// base lib
function searchEventParent() {
    searchEvent();
}
// read query string from url
$.extend({
  getUrlVars: function(){
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(var i = 0; i < hashes.length; i++)
    {
      hash = hashes[i].split('=');
      vars.push(hash[0]);
      vars[hash[0]] = hash[1];
    }
    return vars;
  },
  getUrlVar: function(name){
    return $.getUrlVars()[name];
  }
});
// main search function
var searchEvent = function(jumpPage, rows, initKeyword) {
    var keyword;
    if (initKeyword !== undefined && initKeyword !== "") {
        keyword = initKeyword;
    } else {
        keyword = $("#searchKeyword").val();
    }
    var dateSearchType = $("#dateSearch").val();
    var annual = $("#annualSearch").val();
    var categoryId = $("#categorySearch").val();
    
    // this is list value
    var tagId = "0";   
    var tagvalues = $("#taggroups input").each(function(){
    	tagId = tagId + "," + $(this).val();});    
    var sortColumn = $("#solrSortColumn").val();    
    var sortDirection = $("#solrSortDirection").val();
        
    var data = {'datetype':dateSearchType,'annual':annual,'type':categoryId,'tag':tagId};
    data['sortcolumn'] = sortColumn;
    data['sortdirection'] = sortDirection;    
    
    if (keyword === undefined || keyword === null || keyword === "") {
           data['searchabletext'] = "";
    } else {
           data['searchabletext'] = keyword;
    }
    if (jumpPage !== undefined && jumpPage !== "") 
    {   var start = jumpPage > 0 ? (jumpPage - 1) * rows : 0;
        data['start'] = start;
        data['size'] = rows;
    } else {
        data['start'] = 0;
        data['size'] =10;
    }        
       var action = $("#ajaxsearch").attr('data-ajax-target');
       // tag selected item's data-name value
       var taged = $(".tagSelectSearch li span.over").first().attr("data-name");
     
       $.post(action, 
           data,
           function(resp) {
                       try {
                showSearchEventResult(resp, true, keyword);
                showResultRemind(keyword, dateSearchType, annual, categoryId,taged);
            }
                       catch(e){alert(e);}
                       },
            'json'); 
//    var searchCount = 0;
//    showResultRemind(keyword, dateSearchType, annual, categoryId,tagId)
};
// export as csv

var ExportEvent = function() {

    var dateSearchType = $("#dateSearch").val();
    var annual = $("#annualSearch").val();    
    // this is list value
    var tagId = "0";   
    var tagvalues = $("#taggroups input").each(function(){
    	tagId = tagId + "," + $(this).val();});    
    var sortColumn = $("#solrSortColumn").val();    
    var sortDirection = $("#solrSortDirection").val();        
    var params = {'datetype':dateSearchType,'annual':annual,'tag':tagId};
    params['sortcolumn'] = sortColumn;
    params['sortdirection'] = sortDirection;
    var action = $("#ajaxexport").attr('data-ajax-target');    
//st
    $.ajax({
    type: "POST",
    url: action,
    data: params,
    success: function(response, status, request) {
        var disp = request.getResponseHeader('Content-Disposition');
        if (disp && disp.search('attachment') != -1) {
            var form = $('<form method="POST" action="' + action + '">');
            $.each(params, function(k, v) {
                form.append($('<input type="hidden" name="' + k +
                        '" value="' + v + '">'));
            });
            $('body').append(form);
            form.submit();   
  }
  }
});
};
//st

var totalCountSearchEvent = 0;
var showSearchEventResult = function(D, u, C) {
//function showSearchEventResult(D, u, C) {
//D json response
// u true
// c keyword
//size batch size
//start batch start
//total return result total

    var a = "";
    var h = "";
    var o = parseInt(D['size'],10);
    var l = parseInt(D['start'],10);
    var p = parseInt(D['total'],10);
    totalCountSearchEvent = p;
    var e = (l + o) > p ? (p - l) : o;

    if (e > 0) {
        generatePageLink(l, o, p); 
       a +=  D['searchresult']; 
    } else {
     $("#bottomPageId").html("");

        a += '<tr class="div_tip">';
        a += '<td class="alert alert-block span12" colspan="7">警告！：没有搜索到您要找的信息。</td></tr>';
    }

$("#searchResultDiv").html(a);
};

function showResultRemind(d, a, c, e,m) {
// d search by keyword
// a search by Date
// c search by annual range
// e search by type
// m search by tag, tag number	
    var b = "";
    if (d === "" && (a != "0" || c != "0" || e != "0" || m != "0")) {
        b = createStringSearch(d, a, c, e,m);
    } else {
        if (d !== "" && (a != "0" || c != "0" || e != "0" || m != "0")) {
            b = createStringSearch(d, a, c, e,m);
        }
    }
    if (d === "" && a == "0" && c == "0" && e == "0" && m=="0") {
        b = "<li class='a'>已选择：</li><li id='show_site_result'></li><li class='info' id='searchresultinfor'>“<span id='keyworkshow'>所有</span>”的信息有“<span id='searchresult_count'>" + totalCountSearchEvent + "</span>”条！</li>";
    }
    if (d !== "" && a == "0" && c == "0" && e == "0" && m=="0") {
        b = "<li class='a'>已选择：</li><li id='show_site_result'></li><li class='info' id='searchresultinfor'>有关“<span id='keyworkshow'>" + d + "</span>”的信息有“<span id='searchresult_count'>" + totalCountSearchEvent + "</span>”条！</li>";
    }
//    document.getElementById("all_result_recordinfo").innerHTML = b
    $("#all_result_recordinfo").html(b);
}

var generatePageLink = function(c, n, a) {
    // c: start n:size  a: total
	  var f = $("#bottomPageId");
    // k pages number
	  var k = Math.floor(a / n) + (a % n === 0 ? 0 : 1);
    if (k === 0) {
        k = 1;
    }
    // l current page number
    var l = Math.floor(c / n) + 1;
    var j = $("#fastPageList");
    j.html("");
    // e fast link
    // d pagenation link 
    var d = "";
    var e = "";
    var m = $("#searchtext").val();
    if (m === undefined || m == null || m === "") {
        m = "";
    }
    if (l <= 1) {
        e += "<li class='previous'><a href='javascript:void(0)'>" +
        		"<span aria-hidden='true'>&larr;</span>前一页</a></li>";
        d += "<li class='disabled'><a href='javascript:void(0)'>首页</a></li>";
        d += "<li class='disabled'><a aria-label='Previous' href='javascript:void(0)'>" +
        		"<span aria-hidden='true'>&laquo;</span></a></li>";
    } else {
        e += "<li class='previous'><a href='javascript:searchEvent(" +
        (l - 1) + ",10)'><span aria-hidden='true'>&larr;</span>前一页</a></li>";
        d += "<li><a href=javascript:searchEvent(1,10)>首页</a></li>" +
        		"<li><a page_over num active href=javascript:searchEvent(" + (l - 1) + ",10) >" +
        		"<span aria-hidden='true'>&laquo;</span></a></li>";
    }
    e += "<li><span>" + l + "/" + k + "</span></li>";
    var b = 1;
    var h = 3;
    if (l == 1) {
        b = 1;
        h = l + 2;
        if (h >= k) {
            h = k;
        }
    } else {
        if (l == k) {
            b = k - 2;
            if (b <= 0) {
                b = 1;
            }
            h = k;
        } else {
            b = l - 1;
            h = l + 1;
        }
    }
    for (var g = b; g <= h; g++) {
        if (l == g) {
            d += "<li class='active'><a href='#'>" + g + "</a></li>";
        } else {
            d += "<li><a href=javascript:searchEvent(" + g + ",10) class='page num'>" + g + "</a></li>";
        }
    }
    if (l == k || k < 2) {
        e += "<li class='next'><a href='javascript:void(0)'><span aria-hidden='true'>&rarr;</span> 下一页</a></li>";
        d += "<li class='disabled'><a href='javascript:void(0)' >" +
        		"<span aria-hidden='true'>&raquo;</span></a></li>";
        d += "<li class='disabled'><a href='javascript:void(0)' >末页</a></li>";
    } else {
        e += "<li class='next'><a href='javascript:searchEvent(" + (l + 1) + ",10)'><span aria-hidden='true'>&rarr;</span> 下一页</a></li>";
        d += "<li><a href=javascript:searchEvent(" + (l + 1) + ",10)><span aria-hidden='true'>&raquo;</span></a>" +
        		"<li><a href=javascript:searchEvent(" + (k) + ",10) >末页</a></li>";
    }
   f.html(d);
   j.html(e);
};


function createStringSearch(d, a, c, g,m) {
	// a:selected date number,c:selected annual range ,g:task type key,m:tag number 
    var b = "<li class='a'>已选择：</li><li id='show_site_result'>";
    var h = "";
    switch (a) {
    case "1":
        h = "最近一周";
        b += "<div class='select' onclick=\"closeSearchEventsDiv(1)\" >时间：<button type='button' class='close' aria-label='Close'><span aria-hidden='true'>" + h + "&times;</span></button></div>";
        break;
    case "2":
        h = "最近一月";
        b += "<div class='select' onclick=\"closeSearchEventsDiv(1)\" >时间：<button type='button' class='close' aria-label='Close'><span aria-hidden='true'>" + h + "&times;</span></button></div>";
        break;
    case "3":
        h = "最近一年";
        b += "<div class='select' onclick=\"closeSearchEventsDiv(1)\">时间：<button type='button' class='close' aria-label='Close'><span aria-hidden='true'>" + h + "&times;</span></button></div>";
        break;
    case "4":
        h = "30天内";
        b += "<div class='select' onclick=\"closeSearchEventsDiv(1)\">时间：<button type='button' class='close' aria-label='Close'><span aria-hidden='true'>" + h + "&times;</span></button></div>";
        break;
    case "5":
        h = "30天后";
        b += "<div class='select' onclick=\"closeSearchEventsDiv(1)\">时间：<button type='button' class='close' aria-label='Close'><span aria-hidden='true'>" + h + "&times;</span></button></div>";
        break;
    }
    // annual range
    var f = "";
    if (c == "0") {
        f = "所有";
    } else {
        f = $("#annualRangeSearchUl").find("span[data-name='" + c + "'] a").html();
        b += "<div class='select' onclick=\"closeSearchEventsDiv(2)\">申报年度：<button type='button' class='close' aria-label='Close'><span aria-hidden='true'>" + f + "&times;</span></button></div>";
    }
    //task type
    var e = "";
    if (g == "0") {
        e = "所有";
    } else {
        e = $("#categorySelectSearch").find("span[data-name='" + g + "'] a").html();
        b += "<div class='select' onclick=\"closeSearchEventsDiv(3)\">任务类别：<button type='button' class='close' aria-label='Close'><span aria-hidden='true'>" + e + "&times;</span></button></div>";
    }
    //tag
    var n = "当前标签";
    if (m == "0") {
        n = "所有";
    } else {
    	//n = $(".tagSelectSearch").first().find("span[data-name='" + m + "'] a").html();
		n = "当前标签";

     b += "<div class='select' onclick=\"closeSearchEventsDiv(4)\">标签：<button type='button' class='close' aria-label='Close'><span aria-hidden='true'>" + n + "&times;</span></button></div>";
 }   
    
    // keyword
    if (d === "") {
        b += "</li><li class='info' id='searchresultinfor'>的信息有“<span id='searchresult_count'>" + totalCountSearchEvent + "</span>”条！</li>";
    } else {
        b += "</li><li class='info' id='searchresultinfor'>中有关“<span>" + d + "</span>”的信息有“<span id='searchresult_count'>" + totalCountSearchEvent + "</span>”条！<button type='button' class='close' aria-label='Close'><span aria-hidden='true'>&times;</span></button></li>";
    }
    return b;
	}


$(document).ready(function(){
// read query string
// Getting URL var by its nam
    var byName = $.getUrlVar('orgname');
    if (byName === undefined || byName == null || byName === "") {
               searchEvent();
    } else {
               var byName2 = decodeURIComponent(byName);
               $("#searchKeyword").val(byName2);    
               searchEvent();
    }
	// click search button
	//$("#search").on("click","button",function(){ searchEvent();});
	$("#export").on("click",function(){ ExportEvent();});
	//select date range search
    $("#dateRangeSearchUl li").on("click","span",function() {        
                 if ($(this).attr("class") == "title") {} else {
                 	$("#dateRangeSearchUl li> .over a").removeClass("btn-primary").addClass("btn-default");
                    $("#dateRangeSearchUl li> .over").removeClass("over");
                    $(this).addClass("over");
                    $(this).find("a").removeClass("btn-default").addClass("btn-primary");
                    $("#dateSearch").attr("value", $(this).attr("data-name"));
                    searchEvent();}       
       return false;
    });
    // annual range search
    $("#annualRangeSearchUl li").on("click","span",function() {        
                 if ($(this).attr("class") == "title") {} else {
                 	$("#annualRangeSearchUl li> .over a").removeClass("btn-primary").addClass("btn-default");
                    $("#annualRangeSearchUl li> .over").removeClass("over");
                    $(this).addClass("over");
                    $(this).find("a").removeClass("btn-default").addClass("btn-primary");
                    $("#annualSearch").attr("value", $(this).attr("data-name"));
                    searchEvent();}       
       return false;
    });    
    // security level
   $("#securityLevelSelectSearch li").on("click","span",function() {
                if ($(this).attr("class") == "title" || $(this).attr("class") == "more") {} else 
                {
                    $("#securityLevelSelectSearch li> .over").removeClass("over");
                    $(this).addClass("over");
                    $("#securityLevelSearch").attr("value", $(this).attr("data-name"));
                    searchEvent();
                }
       return false; 
    }); 
   // task type
   $("#categorySelectSearch li").on("click","span",function() {    
                    if ($(this).attr("class") == "title" || $(this).attr("class") == "more") {} else 
                    {
                    $("#categorySelectSearch li> .over").removeClass("over");
                    $(this).addClass("over");
                    $("#categorySearch").attr("value", $(this).attr("data-name"));
                    searchEvent();
                }
       return false; 
    });                 
   // tag area 
   $(".tagSelectSearch li").on("click","span",function() {    
      //if ($(this).attr("class") == "title" || $(this).attr("class") == "more") {} else
      if ($(this).attr("class") == "more") {
		// loadmore       	
   		var start = $(this).attr('data-start');
   		var category = $(this).attr('data-group');
    	var action = $("#ajaxmore").attr('data-ajax-target');
    	var senddata = {'start':start,'category':category};
    	$(this).addClass("running");
    	$.post(action, 
           senddata,
           function(data) {
           	try {
                $(".running").hide();
                var str = data;
                $(str).appendTo($(".running").parent());
                $(".running").remove();            
            	} 
            catch (e) {
                alert(e);
            	}
           },
           'json');
    	return false;       	
      	
      } else  {                    
                    $(this).parent().parent().find(".over a").removeClass("btn-primary").addClass("btn-default");
                    $(this).parent().parent().find(".over").removeClass("over");
                    var newval = $(this).parent().parent().find("input").attr("data-category") + $(this).find("a").html();
                    $(this).parent().parent().find("input").attr("value",newval);
                    $(this).addClass("over");
                    $(this).find("a").removeClass("btn-default").addClass("btn-primary");                    
                    $("#tagSearch").attr("value",newval );
                    //$(this).parent().parent().addClass('running');
                    searchEvent();
                    //$(".running").removeClass('running');
                }
       return false; 
    });  	     
       
   // sort operation
   $("#eventListSort").on("click","a",function() {             
                $("#solrSortColumn").attr("value", $(this).attr("data-name"));
                //a reverse,will be ascending
                if ($(this).attr("class") == "a") {
                    $(this).attr("class", "b");
                    $(this).find("span.glyphicon").addClass("glyphicon-arrow-down").removeClass("glyphicon-arrow-up");
                    $("#solrSortDirection").attr("value", "ascending");
                } else {
                    $(this).attr("class", "a");
                    $(this).find("span.glyphicon").addClass("glyphicon-arrow-up").removeClass("glyphicon-arrow-down");
                    $("#solrSortDirection").attr("value", "reverse");
                }
                searchEvent();
       return false; 
        });  
                 
});
