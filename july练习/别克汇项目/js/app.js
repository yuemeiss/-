// 详情 页

$(function () {
    showhide();
    hvoerSubMenu();
    search();
    share();
    address();
    clickTabs();
    hoverMiniCart();
    clickProductTabs();
    moveMiniImg();
    hoverMiniImg();
    bigImg();

    //  当鼠标在中图上移动时,显示对应大图的附近部分区域
    function bigImg() {
        var $mediumImg = $('#mediumImg');//中图
        var $mask = $('#mask');//小黄块
        var $maskTop = $('#maskTop'); //hover事件发生的容器范围
        var $largeImgContainer = $('#largeImgContainer'); //大图容器范围
        var $loading = $('#loading');//加载中图片
        var $largeImg = $('#largeImg');//大图
        var maskWidth = $mask.width();//黄框的宽
        var maskHeight = $mask.height();//黄快的高　
        var maskTopWidth = $maskTop.width();//中图片的宽
        var maskTopHeight = $maskTop.height();//中图片的高
        $maskTop.hover(function () {
            //鼠标移入,显示小黄块
            $mask.show();
            //动态加载对应的的大图
            var src = $mediumImg.attr('src').replace('-m', '-l');
            $largeImg.attr('src', src);
            //显示大图容器
            $largeImgContainer.show();
            //大图完成的监听
            $largeImg.on('load', function () {
                // 得到大图的尺寸
                var largeWidth = $largeImg.width();
                var largeHeight = $largeImg.height();
                //设置大图容器尺寸
                $largeImgContainer.css({
                    width:largeWidth/2,
                    height:largeHeight/2
                })
                //显示大图
                $largeImg.show();
                // 隐藏加载进度条
                $loading.hide();
                //鼠标移动的监听
                $maskTop.mousemove(function (event) {//在移动的
                    //计算出小黄块的ｌｅｆｔ和ｔｏｐ
                    var left = 0;
                    var top = 0;
                    //事件的坐标
                    var eventLeft = event.offsetX;
                    var eventTop = event.offsetY;
                    left = eventLeft - maskWidth / 2;
                    top = eventTop - maskHeight / 2;
                    //限制小黄块
                    if (left < 0) {
                        left = 0;
                    } else if (left > maskTopWidth - maskWidth) {
                        left = maskTopWidth - maskWidth;
                    }
                    if (top < 0) {
                        top = 0;
                    } else if (top > maskTopHeight - maskHeight) {
                        top = maskTopHeight - maskHeight;
                    }
                    //给小黄快重新定位
                    $mask.css({ left: left, top: top });
                    //大图的移动
                    left = -left * largeWidth / maskTopWidth;
                    top = -top * largeHeight / maskTopHeight;
                    //设置大图的坐标
                    $largeImg.css({left:left,top:top})
                });
               
                
            })



        }, function () {
            //鼠标移出,隐藏小黄块
            $mask.hide();
             //设置大图和容器的的隐藏
             $largeImg.hide();
             $largeImgContainer.hide();
        })

    }

    // 当鼠标悬停在某个小图上, 在上方显示对应的中图
    function hoverMiniImg() {
        $('#icon_list>li').hover(function () {
            var $img = $(this).children();
            $img.addClass('hoveredThumb');
            //显示对应的中图
            var src = $img.attr('src').replace('.jpg', '-m.jpg');
            $('#mediumImg').attr('src', src);
        }, function () {
            $(this).children().removeClass('hoveredThumb');
        })
    }





    // 点击向左/向右 移动当前展示商品的小图片
    function moveMiniImg() {
        var $btns = $('#preview>h1>a');
        var $backward = $btns.first();
        var $forward = $btns.last();
        var $ul = $('#icon_list');
        var SHOW_COUNT = 5;// 一次能显示几个图片
        var imgCount = $ul.children('li').length;//总图片数
        var moveCount = 0;//移动的次数(点右箭头为正数,向左为负数)
        var liWidth = $ul.children(':first').width(); //每次移动的宽度
        //初始化更新
        if (imgCount > SHOW_COUNT) {
            $forward.attr('class', 'forward');
        }
        //给向右的按钮绑定点击监听
        $forward.click(function () {
            //判断是否需要移动,如果不需要直接结束
            if (moveCount === imgCount - SHOW_COUNT) {
                return;
            }
            moveCount++;
            //更新向左的按钮
            $backward.attr('class', 'backward');
            //更新向右的按钮
            if (moveCount === imgCount - SHOW_COUNT) {
                $forward.attr('class', 'forward_disabled');
            }
            //移动ul
            $ul.css({ left: -moveCount * liWidth })

        });
        //给向左的按钮绑定点击监听
        $backward.click(function () {
            //判断是否需要移动,如果不需要直接结束
            if (moveCount === 0) {
                return;
            }
            moveCount--;
            //更新向右的按钮
            $forward.attr('class', 'forward');
            //更新向右的按钮
            if (moveCount === 0) {
                $backward.attr('class', 'backward_disabled');
            }
            //移动ul
            $ul.css({ left: -moveCount * liWidth })

        });
    }






    //  点击切换产品选项(商品详情等)
    function clickProductTabs() {
        var $lis = $('#product_detail>ul>li');
        var $contents = $('#product_detail>div:gt(0)')
        $lis.click(function () {
            $(this).addClass('current').siblings().removeClass('current');
            var index = $(this).index();
            $contents.eq(index).show().siblings(':gt(1)').hide();
        })
    }

    // 鼠标移入移出切换显示迷你购物车
    function hoverMiniCart() {
        $('#minicart').hover(function () {
            $(this).addClass('minicart')
                .children(':last').show();
        }, function () {
            $(this).removeClass('minicart')
                .children(':last').hide();
        })
    }

    // 地址选项卡
    function clickTabs() {
        $('#store_tabs>li').click(function () {
            $(this).addClass('hover').siblings().removeClass('hover');
        })
    }
    // 鼠标移入移出切换地址的显示隐藏
    function address() {
        var $select = $('#store_select');
        $select.hover(function () {
            $(this).children(':gt(0)').show();
        }, function () {
            $(this).children(':gt(0)').hide();
        }).children(':last').click(function () {
            $select.children(':gt(0)').hide();
        })
    }

    // 点击显示或隐藏更多的分享图标
    function share() {
        var isOpen = false;//标识当前事件的状态(初始为关闭)
        var $shareMore = $('#shareMore');
        var $parent = $shareMore.parent();
        var $as = $shareMore.prevAll('a:lt(2)');
        var $b = $shareMore.children();
        $('#shareMore').click(function () {
            if (isOpen) {//打开状态,去关闭
                $parent.css('width', 155);
                $as.hide();
                $b.removeClass('backword');
            } else {//关闭状态,去打开
                $parent.css('width', 200);
                $as.show();
                $b.addClass('backword');
            }
            isOpen = !isOpen;
        });
    }

    // 输入搜索关键字,列表显示匹配的结果
    function search() {
        $('#txtSearch').on('keyup focus', function () {
            // 如果输入文本框有文本才显示表
            var txt = $.trim(this.value);//trim 去除首尾空格
            if (txt) {
                $('#search_helper').show()
            }
        }).blur(function () {
            $('#search_helper').hide()
        })

    }

    // 鼠标移动切换二级导航菜单的切换显示和隐藏
    function hvoerSubMenu() {
        $('#category_items>div').hover(function () {
            // 显示
            $(this).children(':last').show()
        }, function () {
            // 隐藏
            $(this).children(':last').hide()

        })
    }
    // 鼠标移入显示 移除隐藏
    function showhide() {
        $('[name=show_hide]').hover(function () {
            // 显示
            var id = this.id + '_items';
            $('#' + id).show()
        }, function () {
            // 隐藏
            var id = this.id + '_items';
            $('#' + id).hide()

        })
    }







})