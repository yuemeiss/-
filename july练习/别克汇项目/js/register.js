$(function(){
	var error_name = false;//默认没有错误
	var error_pwd = false;
	var error_cpwd = false;
	var error_email = false;
	var error_allow = false;//判断是否勾选了协议

	//失去焦点时验证用户名
	$('#username').blur(function(){
		check_username();
	});

	//获取焦点时隐藏提示信息
	$('#username').focus(function(){
		$(this).prev().hide();
	});

	//密码
	$('#password1').blur(function(){
		check_pwd();
	});
	$('#password1').focus(function(){
		$(this).prev().hide();
	});

	//确认密码
	$('#password2').blur(function(){
		check_cpwd();
	});
	$('#password2').focus(function(){
		$(this).prev().hide();
	});

	//邮箱
	$('#email').blur(function(){
		check_email();
	});
	$('#email').focus(function(){
		$(this).prev().hide();
	});

	//协议
	$('#allow').click(function() {
		//如果复选框是已勾选
		if($(this).prop('checked')){
			error_allow = false;
			$('.error_tip2').hide();
		}else{
			error_allow = true;
			$('.error_tip2').html('请勾选同意！').show();
		}
	});

	function check_username(){
		var val = $('#username').val().trim();
		var re = /^\w{5,15}$/i;//匹配字母数字下划线，5-15位，忽略大小写

		if (val == '') {
			$('#username').prev().html('用户名不能为空！').show();
			error_name = true;
			return;
		}

		if(re.test(val)){//匹配上了就是正确的
			error_name = false;
		}else{
			$('#username').prev().html('用户名是包含数字、字母、下划线的5-15位字符').show();
			error_name = true;
			return;
		}
	}

	function check_pwd(){
		var val = $('#password1').val().trim();
		//[]表示范围，范围内的是允许的
		//允许6-16位的字母数字@$*!?.
		//\u4e00-\u9fa5中文
		var re = /^[a-zA-Z0-9@\$\*\!\?\.]{6,16}$/;

		if (val == '') {
			$('#password1').prev().html('密码不能为空！').show();
			error_pwd = true;
			return;
		}

		if(re.test(val)){//匹配上了就是正确的
			error_pwd = false;
		}else{
			$('#password1').prev().html('密码是包含数字、字母、@$*!?.的6-16位字符').show();
			error_pwd = true;
			return;
		}
	}

	function check_cpwd(){
		var val = $('#password1').val().trim();
		var cval = $('#password2').val().trim();

		if(val == cval){//如果一致是正确的
			error_cpwd = false;
		}else{
			$('#password2').prev().html('再次输入的密码不一致！').show();
			error_cpwd = true;
			return;
		}
	}

	function check_email(){
		var val = $('#email').val().trim();
		//16586445@qq.com  adf@asf.com.cn
		//字母或数字开头、0到多个字母数字下划线小数点、@
		//字母数字下划线、.字母2-3位、小括号是分组，可以有1-2组
		var re = /^[a-zA-Z0-9][\w\.]*@[\w]+(\.[a-z]{2,3}){1,2}$/;

		if (val == '') {
			$('#email').prev().html('邮箱不能为空！').show();
			error_email = true;
			return;
		}

		if(re.test(val)){//匹配上了就是正确的
			error_email = false;
		}else{
			$('#email').prev().html('邮箱格式不正确').show();
			error_email= true;
			return;
		}
	}

	$('.form').submit(function() {
		check_username();
		check_pwd();
		check_cpwd();
		check_email();

		if(!(error_name == false && error_pwd == false 
			&& error_cpwd == false && error_email == false 
			&& error_allow == false)){
			return false;//不能提交
		}
	});
})