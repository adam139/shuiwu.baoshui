$(document).ready(function(){
		//single click modify checkbox 
    $('.checkbox').on('click','.switch-style', function(){
		var shenbaofou = 'true';
		var number = $(this).attr('data-num');
		var checkboxID = $(this).siblings('input');
		if (checkboxID.is(':checked')) {
		checkboxID.prop('checked', false);
		shenbaofou = 'false';	
		}
		else {
		checkboxID.prop('checked', true);
		$(this).css({"color":"red"});
		}
		var action = $(this).attr('data-url');
		var data = {'shenbaofou':shenbaofou,'number':number};		
		//located parent object and add css class
		//$(this).parent().addClass("current");
		$.post(action,data,function(callback) {
			if (callback['result']) {
				$("#ajax-status-notify div").html(callback['message']);
				//$("#ajax-status-notify").show();
			}				
		},'json');
		return false;	
		});
		
// modify nashuiren property		
		$(".p-checkbox").on("click",'.switch-style',function() {
		var checkboxID = $(this).siblings('input');
		var shenbaofou = 'true';
		var property = $(this).attr('data-property');
		if (checkboxID.is(':checked')) {
		checkboxID.prop('checked', false);
		shenbaofou = 'false';	
		}
		else {
		checkboxID.prop('checked', true);
		$(this).css({"color":"red"});
		}
		var action = $("#ajax-target").attr('data-target') + "/@@modify_property";
		var data = {'shenbaofou':shenbaofou,'property':property};	
		$.post(action,data,function(callback) {
			if (callback['result']) {
				$("#ajax-status-notify div").html(callback['message']);
				//$("#ajax-status-notify").show();
			}				
		},'json');
		return false;	
		});
//modify description
		$(".modifydes").on("click",'.description',function() {
		$(this).addClass("editing");
		$(this).parent().parent().addClass("current");
    // display description enter form
    $(".current .ajaxdes").show();
    $(".current .other").hide();
    return false;
    });
    //form ok button
    $(".table").on("click",".current button[name='ok']",function() {		
		//var id = $(this).attr('data-id');
		var old = $(".current .editing").html();
		var description = $(this).parent().find('input').val();
		if (old == description) {
         $(".current .ajaxdes").hide();
         $(".current .other").show();
        	$(".current .editing").removeClass("editing");
        	$(".current").removeClass("current");		
		    return false;
		}		
		var id = $(".current .editing").attr('data-id');
		var action = $("#ajax-target").attr('data-target') + "/@@modify_description";
		var data = {'description':description,'subobj_id':id};	
		$.post(action,data,function(callback) {
			if (callback['result']) {
			$(".current .editing").html(description);
         	$(".current .ajaxdes").hide();
         	$(".current .other").show();
        	$(".current .editing").removeClass("editing");
        	$(".current").removeClass("current");		
			$("#ajax-status-notify div").html(callback['message']);
			//$("#ajax-status-notify").show();
			}				
		},'json');
		return false;	
		});
		//form cancel button
    $(".table").on("click",".current button[name='cancel']",function() {
         $(".current .ajaxdes").hide();
         $(".current .other").show();
         $(".current .editing").removeClass("editing");
         $(".current").removeClass("current");
		return false;        		
        	});						
// modify number
		$(".number-row").on('click','.number',function() {
		$(this).addClass("focus");
		$(this).parent().parent().parent().addClass("running");
    // display number enter form
    $(".running .form").show();
    $(".running .number-row").hide();
    return false;
    });
    $(".bottom").on("click",".running button[name='ok']",function() {
    	var old = $(".running .focus").html();
    	var number = $(".running .focus").attr('data-num');
		var action = $(".running .focus").attr('data-url') + "/@@modify_ancijilu";
		var shenbaocishu = $(this).parent().find('input').val();
		if (old == shenbaocishu) {
         $(".running .form").hide();
         $(".running .number-row").show();
        	$(".running .focus").removeClass("focus");
        	$(".running").removeClass("running");		
		    return false;
		}
		var data = {'shenbaocishu':shenbaocishu,'number':number};
		$.post(action,data,function(callback) {
			if (callback['result']) {
			  $(".running .focus").html(shenbaocishu);
			  $(".running .focus").css({"color":"red"});
         $(".running .form").hide();
         $(".running .number-row").show();
        	$(".running .focus").removeClass("focus");
        	$(".running").removeClass("running");		
			$("#ajax-status-notify div").html(callback['message']);
			//$("#ajax-status-notify").show();
			}				
		},'json');
		return false;	
		});	
    $(".bottom").on("click",".running button[name='cancel']",function() {
         $(".running .form").hide();
         $(".running .number-row").show();
        	$(".running .focus").removeClass("focus");
        	$(".running").removeClass("running");
		return false;        		
        	});   
    //select batch modify		
	$(".outer").on("click",".selectall",function() {
		var url = $("#ajax-target").attr('data-target') + "/@@batch_modify";
		var number = $(this).attr('data-num');
		var actionid = $(this).siblings('.data').attr('data-id');
		$(this).find('input').prop('checked', true);		
		$(this).siblings('.data').find('input').prop('checked', true);
		$(this).siblings('.data').find('span').css({"color":"red"});
        var action = "selectall";
		var data = {'objid':actionid,'action':action,'number':number};
		$(this).addClass('unselectall').removeClass('selectall');
		$.post(url,data,function(callback) {
			if (callback['result']) {
				$("#ajax-status-notify div").html(callback['message']);
				//$("#ajax-status-notify").show();
			}				
		},'json');
		return false;
	});

	$(".outer").on("click",".unselectall",function() {
		var url = $("#ajax-target").attr('data-target') + "/@@batch_modify";
		var number = $(this).attr('data-num');
		var actionid = $(this).siblings('.data').attr('data-id');
		$(this).find('input').prop('checked', false);
		$(this).siblings('.data').find('input').prop('checked', false);
        var action = "unselectall";
		var data = {'objid':actionid,'action':action,'number':number};
		$(this).addClass('selectall').removeClass('unselectall');
		$.post(url,data,function(callback) {
			if (callback['result']) {
				$("#ajax-status-notify div").html(callback['message']);
				//$("#ajax-status-notify").show();
			}				
		},'json');
		return false;
	});			
}
);