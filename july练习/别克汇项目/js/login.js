$(function () {
    VType();
    changeLogin();

    // var address = document.referrer

    // 登录成功　跳转上一夜
    // <a href="javascript:history.back()"></a>
    // alert(address)
    // $('.form').attr('action','#')
    function changeLogin(){
        var scan_login = $('.login-change a:first');
        var acc_login = $('.login-change>a:last');
        
        scan_login.click(function(){
            $(this).parent().find('.scan-login').slideDown().next('div').slideUp();
            scan_login.addClass('style-red');
            acc_login.removeClass('style-red');
        })
        acc_login.click(function(){
            $(this).parent().find('.form_con').slideDown().prev().slideUp();
            acc_login.addClass('style-red');
            scan_login.removeClass('style-red');

        }) 
    }






    //表单验证
    function VType() {
        var error_name = false; //默认没有错误
        var error_pwd = false;

        //失去焦点时验证用户名
        $('#account').blur(function () {
            check_username();
        });

        //获取焦点时隐藏提示信息
        $('#account').focus(function () {
            $(this).parent().prev('span').hide();
        });

        //密码
        $('#password').blur(function () {
            check_pwd();
        });
        $('#password').focus(function () {
            $(this).parent().prev('span').hide();
        });

        function check_username() {
            var val = $('#account').val().trim();
            var re = /^\w{5,15}$/i; //匹配字母数字下划线，5-15位，忽略大小写

            if (val == '') {
                $('#account').parent().prev('span').html('用户名不能为空！').show();
                error_name = true;
                return;
            }

            if (re.test(val)) { //匹配上了就是正确的
                error_name = false;
            } else {
                $('#account').parent().prev('span').html('用户名是包含数字、字母、下划线的5-15位字符').show();
                error_name = true;
                return;
            }
        }

        function check_pwd() {
            var val = $('#password').val().trim();
            //[]表示范围，范围内的是允许的
            //允许6-16位的字母数字@$*!?.
            //\u4e00-\u9fa5中文
            var re = /^[a-zA-Z0-9@\$\*\!\?\.]{6,16}$/;

            if (val == '') {
                $('#password').parent().prev('span').html('密码不能为空！').show();
                error_pwd = true;
                return;
            }

            if (re.test(val)) { //匹配上了就是正确的
                error_pwd = false;
            } else {
                $('#password').parent().prev('span').html('密码是包含数字、字母、@$*!?.的6-16位字符').show();
                error_pwd = true;
                return;
            }
        }
        $('.form').submit(function () {
            check_username();
            check_pwd();

            if (!(error_name == false && error_pwd == false)) {
                return false; //不能提交
            }

        });

    }


})