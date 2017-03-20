# -*- coding: utf-8 -*-
s = '''
<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge" /><meta http-equiv="Cache-Control" content="no-transform" /><meta http-equiv="Cache-Control" content="no-siteapp" /><meta http-equiv="Content-language" content="zh-CN" /><meta name="format-detection" content="telephone=no" /><meta name="applicable-device" content="pc"><link rel="alternate" media="only screen and (max-width: 640px)" href="" >
<meta name="mobile-agent" content="format=html5;url="><script>
ljConf = {
    city_id: '510100',
    city_abbr: 'cd',
    city_name: '成都',
    channel: 'xiaoqu',
    page: 'xiaoqu_list',
    pageConfig: {"ajaxroot":"\/\/ajax.api.lianjia.com\/","imAppid":"LIANJIA_WEB_20160624","imAppkey":"6dfdcee27d78b1107fceeca55d80b7bd"},
    feroot: '//s1.ljcdn.com/feroot/',
    ucid:'',
    cdn:'1',
};
</script>

<script type='text/javascript'>
      var _vds = _vds || [];
      window._vds = _vds;
      (function(){
        _vds.push(['setAccountId', 'a1a50f141657a94e']);
        (function() {
          var vds = document.createElement('script');
          vds.type='text/javascript';
          vds.async = true;
          vds.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'dn-growing.qbox.me/vds.js';
          var s = document.getElementsByTagName('script')[0];
          s.parentNode.insertBefore(vds, s);
        })();
      })();
</script>
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?660aa6a6cb0f1e8dd21b9a17f866726d";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>
<title>成都小区二手房(成都链家网)</title>
<meta name="description" content="链家网成都小区频道,现有成都小区9574个.小区频道提供小区的二手房、租房、信息及成都热门小区的排行情况.为您挑选小区提供便利,并提供小区户型功能,方便您找到适合自己的房子." />
<meta name="keywords" content="成都小区,成都小区,成都小区房源,成都小区二手房,成都小区租房" />
<link href="/favicon.ico" type="image/x-icon" rel=icon><link href="/favicon.ico" type="image/x-icon" rel="shortcut icon"><link rel="stylesheet" href="http://s1.ljcdn.com/feroot/pc/asset/common.css?_v=20170317185744">
<link rel="stylesheet" href="http://s1.ljcdn.com/feroot/pc/asset/ershoufang/xiaoquList/index.css?_v=20170317185744">
<!--[if lt IE 9]><script type="text/javascript" src="http://s1.ljcdn.com/feroot/dep/common-require/html5.js?_v=20170317185744"></script><![endif]-->
<script>
function RESIZEIMG(b,k,l,m){var c=b.parentNode;var d=parseInt(c.offsetWidth)||k;var e=parseInt(c.offsetHeight)||l;var f=d/e;var g=b.naturalWidth||b.width;var h=b.naturalHeight||b.height;var i=g/h;var j="width";if(f<i){j="height";try{b.style["left"]="-"+parseInt(Math.abs((d-(g*e/h))/2))+"px"}catch(e){}}else if(m){try{b.style["top"]="-"+parseInt(Math.abs((e-(h*d/g))/2))+"px"}catch(e){}};b.style[j]="100%";};
</script>
<script>
var _czc = _czc || [];
_czc.push(["_setAccount", "1254525948"]);
</script>

<script type="text/javascript">
var _smq = _smq || [];
_smq.push(['_setAccount', '41331c2', new Date()]);
_smq.push(['_setDomainName', 'lianjia.com']);
_smq.push(['pageview']);
(function() {
var sm = document.createElement('script'); sm.type = 'text/javascript'; sm.async = true;
sm.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'cdnmaster.com/sitemaster/collect.js';
var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(sm, s);
})();
</script>
</head><body><script>
__STAT_LJ_CONF = {
    params: {
        ljweb_group: ['SEARCH','BIGDATA_PC'],
        ljweb_id: '',
        ljweb_mod: '',
        ljweb_bl: '',
        ljweb_el: '',
        ljweb_sl: '',
        ljweb_index: '',
        ljweb_value: '',
        ljweb_url: '',
        ljweb_ljref: (document.cookie.match(/(?:^| )ljref=([^;]*)(?:;|$)/) || ['',''])[1],
        ljweb_sample: (document.cookie.match(/(?:^| )sample_traffic_test=([^;]*)(?:;|$)/) || ['',''])[1],
        ljweb_ref: document.referrer,
        ljweb_cid: '510100',
        ljweb_channel: 'xiaoqu',
        ljweb_page: 'xiaoqu_list'
    }
};



var UT = {
    send: function() {

    }
};
var LjUserTrack = {
    log: [],
    initInterval: false,
    intervalLog: function() {
        setTimeout(function() {
            if(window.$ULOG && $ULOG.send) {
                for(var i = 0, l = LjUserTrack.log.length; i < l; i++) {
                    LjUserTrack.__send(LjUserTrack.log[i]);
                }

                for(var m = 0, n = LjUserTrack.logIds.length; m < n; m++) {
                    LjUserTrack.__sendId(LjUserTrack.logIds[m]);
                }
            } else {
                LjUserTrack.intervalLog();
            }
        }, 16.7);
    },
    _start_time: +new Date,
    __send: function(data) {
        var evt_id = data.evt_id || '10043';
        if('evt_id' in data) {
            delete data.evt_id;
        }

        $ULOG.send(evt_id, {
            "pid": (window.__UDL_CONFIG && window.__UDL_CONFIG.pid && window.__UDL_CONFIG.pid)||"lianjiaweb",
            "key": window.location.href,
            "action": data
        });
    },
    logIds: [],
    __sendId: function(id) {
        id && $ULOG.send(id, {
            "pid": (window.__UDL_CONFIG && window.__UDL_CONFIG.pid && window.__UDL_CONFIG.pid)||"lianjiaweb",
            "key": window.location.href
        });
    },
    sendId: function(id) {
        if(window.$ULOG && $ULOG.send) {
            LjUserTrack.__sendId(id);
        } else {
            LjUserTrack.logIds.push(id);

            LjUserTrack.initInterval || (LjUserTrack.initInterval = true, LjUserTrack.intervalLog());

        }
    },
    send: function(data, el, config) {

        var utConf = __STAT_LJ_CONF;
        var params = config || utConf.params,
            win = window,
            j;

        data.groupIndex = data.ljweb_group || 0;

        if (params) {
            for (var d in params) {
                if(params[d] !== j && data[d] === j) {
                    data[d] = params[d];
                }
            }
        }

        if(el) {
            this.checkClick(el, data);
        }

        data.ljweb_group = params['ljweb_group'][data.groupIndex || 0];

        delete data.groupIndex;

        if(data.typ) {
            data.ljweb_bl = (data.ljweb_bl || '') + '_' + data.typ;
            delete data.typ;
        }

        if(window.$ULOG && $ULOG.send) {
            LjUserTrack.__send(data);
        } else {
            LjUserTrack.log.push(data);

            LjUserTrack.initInterval || (LjUserTrack.initInterval = true, LjUserTrack.intervalLog());

        }

    },
    checkClick: function(el, data) {

        var TAG_LINK = 'A';
        var href = '';
        var elParent = null;

        href = (el.tagName.toUpperCase() === TAG_LINK ? el.getAttribute("href", 2) : '');
        if(!href && (elParent = el.parentNode) && elParent.nodeType === 1) {
            href = (elParent.tagName.toUpperCase() === TAG_LINK ? elParent.getAttribute("href", 2) : '');
        }

        if(href) {
            data.ljweb_url = href;
        } else {
            data.ljweb_url = data.ljweb_url
                  || el.getAttribute("data-log_url")
                  || (elParent=el.parentNode||el).getAttribute("data-log_url")
                  || (
                        (elParent=elParent.parentNode||elParent)
                     && (elParent.nodeType === 1)
                     && elParent.getAttribute("data-log_url")
                     )
                  || "";
        }

        this.attr(el, data);

    },
    path: function() {

    },
    attr: function(el, data) {
        var modId     = el.getAttribute("log-mod");
        var blAttr    = el.getAttribute("data-bl");
        var elAttr    = el.getAttribute("data-el");
        var slAttr    = el.getAttribute("data-sl");
        var InAttr    = el.getAttribute("data-log_index");
        var valAttr   = el.getAttribute("data-log_value");
        var idAttr    = el.getAttribute("data-log_id");
        var groupAttr = el.getAttribute("data-log_group");
        var evtId     = el.getAttribute("data-log_evtid");

        data.ljweb_bl    = data.ljweb_bl || blAttr || '';
        data.ljweb_el    = data.ljweb_el || elAttr || '';
        data.ljweb_sl    = data.ljweb_sl || slAttr || '';
        data.ljweb_index = data.ljweb_index || InAttr || '';
        data.ljweb_value = data.ljweb_value || valAttr || '';
        data.ljweb_id    = data.ljweb_id || idAttr || '';
        data.groupIndex  = data.groupIndex || groupAttr || 0;
        data.evt_id      = data.evt_id || evtId || '';

        if (!modId) {
            if (el.parentNode && el.parentNode.nodeType === 1 && el.parentNode.tagName.toUpperCase() !== 'BODY') {
                this.attr(el.parentNode, data);
            }
        } else {
            data.ljweb_mod = modId;
        }
    }
};

;;(function() {
    var isW3c = !!document.addEventListener;

    LjUserTrack.send({
        ljweb_mod: 'pv',
        ljweb_group: 1
    });

    /*window[isW3c ? 'addEventListener' : 'attachEvent'](
        (isW3c ? '': 'on') + 'beforeunload',
        function(e) {
            var _end_time = +new Date;
            UT.send({type: 'show', subtype: 'stay', time: (_end_time-UT._start_time)/1000});
        },
        false);*/
})();





</script>
<div class="banner"><div class="container"><ul class="channelList"><li><a href="//www.lianjia.com/">首页</a></li><li  class=""><a href="http://cd.lianjia.com/ershoufang/" >二手房</a></li><li  class=""><a href="http://cd.fang.lianjia.com/" >新房</a></li><li  class=""><a href="http://cd.lianjia.com/zufang/" >租房</a></li><li  rel="nofollow"  class=""><a href="http://you.lianjia.com/" >旅居地产</a></li><li  class=""><a href="http://us.lianjia.com/" >海外</a></li><li  class="selected"><a href="http://cd.lianjia.com/xiaoqu/" >小区</a></li><li  class=""><a href="http://cd.lianjia.com/jingjiren/" >经纪人</a></li><li  class=""><a href="http://news.cd.lianjia.com/baike/" >百科</a></li><li  class=""><a href="http://cd.lianjia.com/fangjia/" >房价</a></li><li  class=""><a href="http://cd.lianjia.com/yezhu/" target="_blank">卖房</a></li></ul><div class="banner-right"><div class="login" id="userInfoContainer"><i></i><a href="https://passport.lianjia.com/cas/login?service=http%3A%2F%2Fcd.lianjia.com%2Fxiaoqu%2F" id="loginBtn">登录</a>/<a href="http://passport.lianjia.com/register/resources/lianjia/register.html?service=http%3A%2F%2Fcd.lianjia.com%2Fxiaoqu%2F" rel="nofollow">注册</a></div><div class="phone"><i></i><span>热线电话1010-9666</span></div></div></div></div>


<script type="text/template" id="userInfoTpl">
  <i></i>
  <%if(isAgent){%>
    <a id="userNameContainer" href="<%=$.env.fixedUrl('//agent.lianjia.com/')%>"><%=username%></a>
  <%}else{%>
    <a id="userNameContainer" href="<%=$.env.fixedUrl('//user.lianjia.com/')%>" rel="nofollow"><%=username%></a>
  <%}%>
  <span id="tipContainer"></span>
  &nbsp;&nbsp;<a href="<%=logoutUrl%>">退出</a>
  <span id="pushNewsListContainer"></span>
</script>
<script type="text/template" id="pushNewsListTpl">
  <div class="pushNewsList">
    <%for(var i in group_by_type){%>
      <%if(group_by_type[i].unread !== 0 && pushMsgMap.hasOwnProperty(i)){%>
        <a href="<%=pushMsgMap[i].url%>"><%=$.replaceTpl(pushMsgMap[i].text, {unread:group_by_type[i].unread})%></a>
      <%}%>
    <%}%>
  </div>
</script>
<div class="header"><div class="menu"><div class="menuLeft"><a href="/ershoufang" class="logo"></a><ul class="typeList"><li ><a href="/ershoufang/"  title="成都在售二手房" >在售</a></li><li ><a href="/chengjiao/"  title="成都成交二手房" >成交</a></li><li class="selected"><a href="/xiaoqu/"  title="成都小区二手房" >小区</a></li><li ><a href="/fangjia/"  title="成都房价二手房" >房价</a></li><li ><a href="/ditu/"  title="成都地图找房二手房" target="_blank">地图找房</a></li></ul></div><div class="app"><a href="//www.lianjia.com/client/" target="_blank"><i></i>下载链家APP</a></div></div><div class="search"><div class="input" log-mod="search"><form id="searchForm" action='/ershoufang/rs'><input type="text" id="searchInput" value="" autocomplete="off"><div class="inputRightPart"><div class="save" id="savedSearchMsg"><span id="savedSearchCount">0</span>条已保存搜索<span id="savedSearchArrow" class="downArrow"></span></div><button type='submit' class="searchButton" data-bl="search" data-el="search">&nbsp;<i></i>&nbsp;</button></div></form><div class="searchMsg" id="searchMsgContainer"></div></div></div></div>


<script type="text/template" id="hotSearchTpl">
  <div class="searchMsgTitle">
    <span class="searchMsgName">热门搜索</span>
  </div>
  <ul data-bl="sug" data-el="history">
    <%for(var i =0; i < list.length; i++){%>
    <li>
      <a role="addHistory" href="<%=list[i].url%>" data-log_index="<%=i+1%>" data-log_value="<%=list[i].string%>" class="sug--search_item">
        <span class="msgListTitle" role="historyKey"><%=list[i].string%></span>
      </a>
    </li>
    <%}%>
  </ul>
</script>
<script type="text/template" id="searchHistoryTpl">
  <div class="searchMsgTitle">
    <span class="searchMsgName">搜索历史</span>
    <div class="searchMsgTitleRightPart">
      <a href="#" id="clearSearchHistory" class="manage">清除历史记录</a>
    </div>
  </div>
  <ul data-bl="sug" data-el="history">
  <%for(var i = 0; i < list.length; i++){%>
    <li>
      <a href="<%=list[i].url%>" role="addHistory" data-log_index="<%=i+1%>" data-log_value="<%=$.encodeHTML(list[i].name)%>" class="sug--search_item">
        <span class="msgListTitle" role="historyKey"><%=$.encodeHTML(list[i].name)%></span>
        <%if(list[i].newCount) {%>
          <span class="msgListAdd"><%=list[i].newCount%>套新增房源</span>
        <%}%>
      </a>
    </li>
  <%}%>
  </ul>
</script>
<script type="text/template" id="searchSuggestionTpl">
  <div class="searchMsgTitle">
    <span class="searchMsgName">你可能在找</span>
  </div>
  <ul data-bl="sug" data-el="sug">
  <%for(var i = 0;i < list.length;i++){%>
    <li>
      <a href="<%=list[i].url%>" role="addHistory" data-log_index="<%=i+1%>" data-log_value="<%=list[i].title%>">
        <span class="msgListTitle">
          <span role="historyKey"><%=list[i].title%></span>
          <%if(list[i].region){%>
            <span class="msgListArea"><%=list[i].region%></span>
          <%}%>
        </span>
        <%if(type === 'sell'){%>
          <span class="msgListAdd">约<%=list[i].count%>套在售</span>
        <%}else if(type === 'deal'){%>
          <span class="msgListAdd">约<%=list[i].count%>套成交</span>
        <%}%>
      </a>
    </li>
  <%}%>
  </ul>
</script>
<script type="text/template" id="savedSearchTpl">
  <div class="searchMsgTitle">
    <span class="searchMsgName">已保存搜索</span>
    <div class="searchMsgTitleRightPart">
    <%if(totalCount){%>
      <a class="totalNew">查看<%=totalCount%>套新增房源</a>
    <%}%>
      <a href="<%=userCenterUrl%>" class="manage">管理</a>
    </div>
  </div>
  <ul data-bl="sug" data-el="history">
    <%for(var i = 0; i < savedData.length; i++){
      var title = savedData[i].query ? savedData[i].query + '&nbsp;' : '';
      title = title + savedData[i].title.join('&nbsp;');
    %>
      <li>
        <a href="<%=savedData[i].url%>" role="savedSearch" data-log_index="<%=i+1%>" data-log_value="<%=title%>" class="sug--search_item">
          <span class="msgListTitle"><%=title%></span>
          <%if(savedData[i].unread && savedData[i].unread !== 0){%>
          <span class="msgListAdd">新增<%=savedData[i].unread%>套</span>
          <%}%>
        </a>
      </li>
    <%}%>
  </ul>
</script>

<script>
  var hotSearchData = {
    channel:[{"name":"\u4e8c\u624b\u623f","action":"ershoufang","channel":"ershoufang","checked":1,"tipsHot":{"query":[{"string":"\u9ad8\u65b0","url":"http:\/\/cd.lianjia.com\/ershoufang\/gaoxin7\/"},{"string":"\u5929\u5e9c\u65b0\u533a","url":"http:\/\/cd.lianjia.com\/fangjia\/tianfuxinqu\/"},{"string":"\u5357\u57ce\u90fd\u6c47","url":"http:\/\/cd.lianjia.com\/xiaoqu\/1611047199431\/"},{"string":"\u5fb7\u5546\u00b7\u534e\u5e9c\u5929\u9a84","url":"http:\/\/cd.lianjia.com\/xiaoqu\/1611063967004\/"},{"string":"\u534e\u6da6\u4e8c\u5341\u56db\u57ce","url":"http:\/\/cd.lianjia.com\/xiaoqu\/3011054427433\/"},{"string":"\u4e1c\u82d1","url":"http:\/\/cd.lianjia.com\/xiaoqu\/1611041786160\/"}],"tips":"\u8bf7\u8f93\u5165\u533a\u57df\u3001\u5546\u5708\u6216\u5c0f\u533a\u540d\u5f00\u59cb\u627e\u623f"}},{"name":"\u5c0f\u533a","action":"xiaoqu","channel":"xiaoqu","checked":0,"tipsHot":{"query":[{"string":"\u53cc\u6960\u5c0a\u90b8","url":"http:\/\/cd.lianjia.com\/xiaoqu\/1611041481079\/"},{"string":"\u5357\u5e9c\u9526","url":"http:\/\/cd.lianjia.com\/xiaoqu\/1611041552349\/"},{"string":"\u534e\u6da6\u51e4\u51f0\u57ce\u4e00\u671f","url":"http:\/\/cd.lianjia.com\/xiaoqu\/3011055412135\/"},{"string":"\u9f99\u57ce\u56fd\u9645","url":"http:\/\/cd.lianjia.com\/xiaoqu\/1611061503509\/"},{"string":"\u7ea2\u724c\u697c\u5e7f\u573a","url":"http:\/\/cd.lianjia.com\/xiaoqu\/1611041495758\/"},{"string":"\u56db\u5b63\u5eb7\u57ce","url":"http:\/\/cd.lianjia.com\/xiaoqu\/3011055910332\/"},{"string":"\u4e2d\u6d77\u57ce\u5357\u4e00\u53f7","url":"http:\/\/cd.lianjia.com\/xiaoqu\/1611047722172\/"},{"string":"\u7eff\u5730\u9526\u5929\u5e9c","url":"http:\/\/cd.lianjia.com\/xiaoqu\/1611047571588\/"}],"tips":"\u8bf7\u8f93\u5165\u5c0f\u533a\u540d\u5f00\u59cb\u67e5\u627e\u5c0f\u533a"}},{"name":"\u65b0\u623f","action":"loupan","channel":"xinfang","checked":0,"tipsHot":{"query":[{"string":"\u83b1\u8335\u5317\u90e1","url":"http:\/\/cd.lianjia.com\/loupan\/p_lybjaaarx\/"},{"string":"\u541b\u96c1\u91d1\u68a7\u6850","url":"http:\/\/cd.lianjia.com\/loupan\/p_jyjwtaaass\/"},{"string":"\u6da6\u626c\u53cc\u94c1\u5e7f\u573a","url":"http:\/\/cd.lianjia.com\/loupan\/p_rystgcaabbo\/"},{"string":"\u5b87\u4f17\u60a6\u57ce","url":"http:\/\/cd.lianjia.com\/loupan\/p_yzycaabcd\/"},{"string":"\u57ce\u7f6e\u5c1a\u8c6a\u5ead","url":"http:\/\/cd.lianjia.com\/loupan\/p_czshtaabbu\/"},{"string":"\u5cf0\u5ea6\u5929\u4e0b","url":"http:\/\/cd.lianjia.com\/loupan\/p_fdtxaaber\/"},{"string":"\u4e2d\u73af\u5c9b","url":"http:\/\/cd.lianjia.com\/loupan\/p_zhdaabft\/"},{"string":"\u5723\u6866\u57ce","url":"http:\/\/cd.lianjia.com\/loupan\/p_shcaabke\/"}],"tips":"\u8bf7\u8f93\u5165\u697c\u76d8\u540d\u79f0\u5f00\u59cb\u627e\u623f"}},{"name":"\u67e5\u623f\u4ef7","action":"fangjia","channel":"fangjia","checked":0,"tipsHot":{"query":[{"string":"\u9752\u7f8a","url":"http:\/\/cd.lianjia.com\/fangjia\/qingyang\/"},{"string":"\u9526\u6c5f","url":"http:\/\/cd.lianjia.com\/fangjia\/jinjiang\/"},{"string":"\u5e9c\u5357\u65b0\u533a","url":"http:\/\/cd.lianjia.com\/fangjia\/funanxinqu\/"},{"string":"\u4e2d\u94c1\u897f\u5b50\u9999\u8377","url":"http:\/\/cd.lianjia.com\/fangjia\/c1611041555455\/"},{"string":"\u4e07\u79d1\u57ce\u5e02\u82b1\u56ed","url":"http:\/\/cd.lianjia.com\/fangjia\/c1611057879617\/"},{"string":"\u534e\u5e9c\u91d1\u6c99","url":"http:\/\/cd.lianjia.com\/fangjia\/c1611041585473\/"},{"string":"\u534e\u6da6\u4e8c\u5341\u56db\u57ce","url":"http:\/\/cd.lianjia.com\/fangjia\/c3011054427433\/"},{"string":"\u65f6\u4ee3\u5c0a\u57ce","url":"http:\/\/cd.lianjia.com\/fangjia\/c1611041601162\/"}],"tips":"\u5357\u57ce\u90fd\u6c47"}},{"name":"\u79df\u623f","action":"zufang","channel":"zufang","checked":0,"tipsHot":{"query":[{"string":"\u9526\u6c5f","url":"http:\/\/cd.lianjia.com\/zufang\/jinjiang\/"},{"string":"\u4e5d\u773c\u6865","url":"http:\/\/cd.lianjia.com\/zufang\/jiuyanqiao\/"},{"string":"\u6b66\u4faf","url":"http:\/\/cd.lianjia.com\/zufang\/wuhou\/"},{"string":"\u51ef\u5fb7\u98ce\u5c1a","url":"http:\/\/cd.lianjia.com\/zufang\/c1611043174238\/"},{"string":"\u7fe1\u7fe0\u57ce\u4e00\u671f","url":"http:\/\/cd.lianjia.com\/zufang\/c1611042527332\/"},{"string":"\u6676\u84dd\u534a\u5c9b","url":"http:\/\/cd.lianjia.com\/zufang\/c1611041544254\/"},{"string":"1\u53f7\u7ebf","url":"http:\/\/cd.lianjia.com\/ditiezufang\/li110460717\/"},{"string":"2\u53f7\u7ebf","url":"http:\/\/cd.lianjia.com\/ditiezufang\/li110460718\/"}],"tips":"\u8bf7\u8f93\u5165\u533a\u57df\u3001\u5546\u5708\u6216\u5c0f\u533a\u540d\u5f00\u59cb\u627e\u623f"}},{"name":"\u7ecf\u7eaa\u4eba","action":"jingjiren","channel":"jingjiren","checked":0,"tipsHot":{"query":[],"tips":"\u8bf7\u8f93\u5165\u5546\u5708\u3001\u5c0f\u533a\u6216\u7ecf\u7eaa\u4eba\u7684\u59d3\u540d\u3001\u7535\u8bdd..."}}],
    curChannel:'ershoufang'
  };
</script>
<div class="m-filter">
      <div class="position">
      <dl>
        <h2><dt title="成都小区位置">位置</dt></h2>
        <dd>
                  <a href="/xiaoqu/" class="selected" title="成都小区区域">
            区域<span class="arrow"></span>
          </a>
                </dd>
      </dl>
      <dl>
        <dt></dt>
        <dd>
          <!-- 区域 -->
                    <div data-role="ershoufang" >
            <div>
                              <a href="/xiaoqu/jinjiang/"  title="成都锦江小区二手房 ">锦江</a>
                              <a href="/xiaoqu/qingyang/"  title="成都青羊小区二手房 ">青羊</a>
                              <a href="/xiaoqu/wuhou/"  title="成都武侯小区二手房 ">武侯</a>
                              <a href="/xiaoqu/gaoxin7/"  title="成都高新小区二手房 ">高新</a>
                              <a href="/xiaoqu/chenghua/"  title="成都成华小区二手房 ">成华</a>
                              <a href="/xiaoqu/jinniu/"  title="成都金牛小区二手房 ">金牛</a>
                              <a href="/xiaoqu/tianfuxinqu/"  title="成都天府新区小区二手房 ">天府新区</a>
                              <a href="/xiaoqu/shuangliu/"  title="成都双流小区二手房 ">双流</a>
                              <a href="/xiaoqu/wenjiang/"  title="成都温江小区二手房 ">温江</a>
                              <a href="/xiaoqu/pidou/"  title="成都郫都小区二手房 ">郫都</a>
                              <a href="/xiaoqu/longquanyi/"  title="成都龙泉驿小区二手房 ">龙泉驿</a>
                              <a href="/xiaoqu/xindou/"  title="成都新都小区二手房 ">新都</a>
                              <a href="/xiaoqu/gaoxinxi1/"  title="成都高新西小区二手房 ">高新西</a>
                          </div>
                      </div>
                    <!-- 地铁 -->
                    <!-- 学区 -->
                  </dd>
      </dl>
    </div>

  <div class="list-more">
                                                                                                                                                                                                                        <dl class=" hasmore" >
          <h2><dt title="成都均价小区二手房">均价</dt></h2>
          <dd>
                                                                    <a href="/xiaoqu/p1/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">0.5万以下</span>
                              </a>
                                                                    <a href="/xiaoqu/p2/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">0.5-0.8万</span>
                              </a>
                                                                    <a href="/xiaoqu/p3/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">0.8-1万</span>
                              </a>
                                                                    <a href="/xiaoqu/p4/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">1-1.5万</span>
                              </a>
                                                                    <a href="/xiaoqu/p5/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">1.5-2万</span>
                              </a>
                                                                    <a href="/xiaoqu/p6/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">2万以上</span>
                              </a>
                                                              <span class="customFilter mt" data-role="price">
                <input type="text" role="minValue" value="">
                <span>-</span>
                <input type="text" role="maxValue" value="">&nbsp;
                                  <span>万</span>
                                <button class="btn-range hide" data-url="/xiaoqu/bp{min}ep{max}/">确定</button>
              </span>
                                                  <span class="btn-showmore">+ 更多及自定义</span>
                      </dd>
        </dl>
                                                                                                                                                          <dl class=" " >
          <h2><dt title="成都楼龄小区二手房">楼龄</dt></h2>
          <dd>
                                                                    <a href="/xiaoqu/y1/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">5年以内</span>
                              </a>
                                                                    <a href="/xiaoqu/y2/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">10年以内</span>
                              </a>
                                                                    <a href="/xiaoqu/y3/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">15年以内</span>
                              </a>
                                                                    <a href="/xiaoqu/y4/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">20年以内</span>
                              </a>
                                                                    <a href="/xiaoqu/y5/" class="" rel="nofollow">
                <span class="checkbox "></span>
                <span class="name">20年以上</span>
                              </a>
                                                          </dd>
        </dl>
                </div>
  </div>
<div class="content"><!-- 左侧内容 --><div class="leftContent"><div class="orderFilter"><div class="orderTag"><ul><li class='selected'><h3><a href="/xiaoqu/">默认排序</span></a></h3></li><li ><h3><a href="/xiaoqu/cro21/">小区均价</a></h3></li><li ><h3><a href="/xiaoqu/cro11/">按成交量</a></h3></li></ul></div><div class="filterAgain"><div class="title">筛选：</div><ul><li ><a href="/xiaoqu/su1/"><span class="checkbox"></span>近地铁</a></li></ul></div></div><div class="resultDes clear"><h2 class="total fl">共找到<span> 9574 </span>个小区</h2><div class="button fr"></div></div><ul class="listContent" log-mod="list"><li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/3011055393438/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/86326feb-bbd5-4eeb-9ff3-9887f47d1738.jpg.232x174.jpg" alt="天鹅湖北苑">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/3011055393438/" target="_blank">天鹅湖北苑</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="天鹅湖北苑网签"  href="http://cd.lianjia.com/chengjiao/c3011055393438/" >90天成交24套</a>
      <span class="cutLine">|</span><a title="天鹅湖北苑租房"  href="http://cd.lianjia.com/zufang/c3011055393438/" >31套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/gaoxin7/" class="district" title="高新小区">高新</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/xinhuizhan/" class="bizcircle" title="新会展小区">新会展</a>&nbsp;
                  /&nbsp;2007年建成
          </div>
        <div class="tagList">
                    <span>近地铁1号线世纪城站</span>
          </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>11641</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="天鹅湖北苑二手房" href="http://cd.lianjia.com/ershoufang/c3011055393438/" class="totalSellCount"><span>27</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/3011056075583/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/37446772-1ecc-4ff2-938c-e4aa03eb9ae5.jpg.232x174.jpg" alt="南湖国际社区">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/3011056075583/" target="_blank">南湖国际社区</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="南湖国际社区网签"  href="http://cd.lianjia.com/chengjiao/c3011056075583/" >90天成交67套</a>
      <span class="cutLine">|</span><a title="南湖国际社区租房"  href="http://cd.lianjia.com/zufang/c3011056075583/" >30套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/tianfuxinqu/" class="district" title="天府新区小区">天府新区</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/nanhu/" class="bizcircle" title="南湖小区">南湖</a>&nbsp;
                  /&nbsp;2010年建成
          </div>
        <div class="tagList">
                </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>10232</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="南湖国际社区二手房" href="http://cd.lianjia.com/ershoufang/c3011056075583/" class="totalSellCount"><span>98</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/1611041540545/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/d9eb85c6-9a81-4b92-b3b7-616c4e0f2ab8.jpg.232x174.jpg" alt="蜀都花园">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/1611041540545/" target="_blank">蜀都花园</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="蜀都花园网签"  href="http://cd.lianjia.com/chengjiao/c1611041540545/" >90天成交57套</a>
      <span class="cutLine">|</span><a title="蜀都花园租房"  href="http://cd.lianjia.com/zufang/c1611041540545/" >31套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/jinjiang/" class="district" title="锦江小区">锦江</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/shuinianhe/" class="bizcircle" title="水碾河小区">水碾河</a>&nbsp;
                  /&nbsp;2002年建成
          </div>
        <div class="tagList">
                    <span>近地铁2号线牛王庙站</span>
          </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>10857</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="蜀都花园二手房" href="http://cd.lianjia.com/ershoufang/c1611041540545/" class="totalSellCount"><span>20</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/1611047233738/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/34d2eb08-de3a-46f4-bcc6-6bf163a8efba.jpg.232x174.jpg" alt="中海翠屏湾">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/1611047233738/" target="_blank">中海翠屏湾</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="中海翠屏湾网签"  href="http://cd.lianjia.com/chengjiao/c1611047233738/" >90天成交26套</a>
      <span class="cutLine">|</span><a title="中海翠屏湾租房"  href="http://cd.lianjia.com/zufang/c1611047233738/" >30套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/gaoxin7/" class="district" title="高新小区">高新</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/chengnanyijia/" class="bizcircle" title="城南宜家小区">城南宜家</a>&nbsp;
                  /&nbsp;2009年建成
          </div>
        <div class="tagList">
                </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>14717</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="中海翠屏湾二手房" href="http://cd.lianjia.com/ershoufang/c1611047233738/" class="totalSellCount"><span>39</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/1611043137543/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/00d5b02a-d541-4926-a48e-24c2907bf8ac.jpg.232x174.jpg" alt="桐梓林欧城">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/1611043137543/" target="_blank">桐梓林欧城</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="桐梓林欧城网签"  href="http://cd.lianjia.com/chengjiao/c1611043137543/" >90天成交10套</a>
      <span class="cutLine">|</span><a title="桐梓林欧城租房"  href="http://cd.lianjia.com/zufang/c1611043137543/" >76套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/wuhou/" class="district" title="武侯小区">武侯</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/tongzilin/" class="bizcircle" title="桐梓林小区">桐梓林</a>&nbsp;
                  /&nbsp;2009年建成
          </div>
        <div class="tagList">
                    <span>近地铁1号线火车南站站</span>
          </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>18280</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="桐梓林欧城二手房" href="http://cd.lianjia.com/ershoufang/c1611043137543/" class="totalSellCount"><span>34</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/1611047722172/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/e6e8a072-1fdd-495e-b373-80dc8c79e379.jpg.232x174.jpg" alt="中海城南一号一期">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/1611047722172/" target="_blank">中海城南一号一期</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="中海城南一号一期网签"  href="http://cd.lianjia.com/chengjiao/c1611047722172/" >90天成交6套</a>
      <span class="cutLine">|</span><a title="中海城南一号一期租房"  href="http://cd.lianjia.com/zufang/c1611047722172/" >17套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/gaoxin7/" class="district" title="高新小区">高新</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/jinrongcheng/" class="bizcircle" title="金融城小区">金融城</a>&nbsp;
                  /&nbsp;2012年建成
          </div>
        <div class="tagList">
                    <span>近地铁1号线金融城站</span>
          </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>29929</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="中海城南一号一期二手房" href="http://cd.lianjia.com/ershoufang/c1611047722172/" class="totalSellCount"><span>21</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/1611043113553/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/502bb262-6a55-456e-b12c-6ba13e74aa13.jpg.232x174.jpg" alt="时代晶科名苑">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/1611043113553/" target="_blank">时代晶科名苑</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="时代晶科名苑网签"  href="http://cd.lianjia.com/chengjiao/c1611043113553/" >90天成交18套</a>
      <span class="cutLine">|</span><a title="时代晶科名苑租房"  href="http://cd.lianjia.com/zufang/c1611043113553/" >20套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/gaoxin7/" class="district" title="高新小区">高新</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/shiyiyiyuan/" class="bizcircle" title="市一医院小区">市一医院</a>&nbsp;
                  /&nbsp;2012年建成
          </div>
        <div class="tagList">
                    <span>近地铁1号线高新站</span>
          </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>16349</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="时代晶科名苑二手房" href="http://cd.lianjia.com/ershoufang/c1611043113553/" class="totalSellCount"><span>36</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/1611050213419/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/0a0c97ac-500c-46eb-bd2d-3dead9dd47ba.jpg.232x174.jpg" alt="龙湖世纪峰景">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/1611050213419/" target="_blank">龙湖世纪峰景</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="龙湖世纪峰景网签"  href="http://cd.lianjia.com/chengjiao/c1611050213419/" >90天成交12套</a>
      <span class="cutLine">|</span><a title="龙湖世纪峰景租房"  href="http://cd.lianjia.com/zufang/c1611050213419/" >15套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/gaoxin7/" class="district" title="高新小区">高新</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/xinhuizhan/" class="bizcircle" title="新会展小区">新会展</a>&nbsp;
                  /&nbsp;2017年建成
          </div>
        <div class="tagList">
                    <span>近地铁1号线世纪城站</span>
          </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>17310</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="龙湖世纪峰景二手房" href="http://cd.lianjia.com/ershoufang/c1611050213419/" class="totalSellCount"><span>45</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/3011056075084/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/72c43005-c3e0-458f-9e31-41e482bef41d.JPG.232x174.jpg" alt="恒大名都">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/3011056075084/" target="_blank">恒大名都</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="恒大名都网签"  href="http://cd.lianjia.com/chengjiao/c3011056075084/" >90天成交36套</a>
      <span class="cutLine">|</span><a title="恒大名都租房"  href="http://cd.lianjia.com/zufang/c3011056075084/" >5套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/tianfuxinqu/" class="district" title="天府新区小区">天府新区</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/haiyanggongyuan/" class="bizcircle" title="海洋公园小区">海洋公园</a>&nbsp;
                  /&nbsp;2010年建成
          </div>
        <div class="tagList">
                </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>10726</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="恒大名都二手房" href="http://cd.lianjia.com/ershoufang/c3011056075084/" class="totalSellCount"><span>20</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/3011055396081/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/7709f036-5518-4fa1-a615-4c8886d7b833.jpg.232x174.jpg" alt="天鹅湖花园">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/3011055396081/" target="_blank">天鹅湖花园</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="天鹅湖花园网签"  href="http://cd.lianjia.com/chengjiao/c3011055396081/" >90天成交17套</a>
      <span class="cutLine">|</span><a title="天鹅湖花园租房"  href="http://cd.lianjia.com/zufang/c3011055396081/" >8套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/gaoxin7/" class="district" title="高新小区">高新</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/xinhuizhan/" class="bizcircle" title="新会展小区">新会展</a>&nbsp;
                  /&nbsp;2008年建成
          </div>
        <div class="tagList">
                    <span>近地铁1号线世纪城站</span>
          </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>10988</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="天鹅湖花园二手房" href="http://cd.lianjia.com/ershoufang/c3011055396081/" class="totalSellCount"><span>26</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/1611041469734/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/41ef346b-d39d-48e2-ae2c-07f30da00d26.JPG.232x174.jpg" alt="武侯国际花园">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/1611041469734/" target="_blank">武侯国际花园</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="武侯国际花园网签"  href="http://cd.lianjia.com/chengjiao/c1611041469734/" >90天成交16套</a>
      <span class="cutLine">|</span><a title="武侯国际花园租房"  href="http://cd.lianjia.com/zufang/c1611041469734/" >4套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/wuhou/" class="district" title="武侯小区">武侯</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/hongpailou/" class="bizcircle" title="红牌楼小区">红牌楼</a>&nbsp;
                  /&nbsp;2009年建成
          </div>
        <div class="tagList">
                </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>8985</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="武侯国际花园二手房" href="http://cd.lianjia.com/ershoufang/c1611041469734/" class="totalSellCount"><span>10</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/1611043451443/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/cc9d2316-e01b-48da-b748-0bcc704ca82a.jpg.232x174.jpg" alt="保利金香槟">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/1611043451443/" target="_blank">保利金香槟</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="保利金香槟网签"  href="http://cd.lianjia.com/chengjiao/c1611043451443/" >90天成交27套</a>
      <span class="cutLine">|</span><a title="保利金香槟租房"  href="http://cd.lianjia.com/zufang/c1611043451443/" >8套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/qingyang/" class="district" title="青羊小区">青羊</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/waijinsha/" class="bizcircle" title="外金沙小区">外金沙</a>&nbsp;
                  /&nbsp;2012年建成
          </div>
        <div class="tagList">
                    <span>近地铁4号线清江西路站</span>
          </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>14474</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="保利金香槟二手房" href="http://cd.lianjia.com/ershoufang/c1611043451443/" class="totalSellCount"><span>7</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/3011055414228/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/8968745f-c77f-4e05-a027-f4d770700caa.jpg.232x174.jpg" alt="慕和南道">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/3011055414228/" target="_blank">慕和南道</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="慕和南道网签"  href="http://cd.lianjia.com/chengjiao/c3011055414228/" >90天成交29套</a>
      <span class="cutLine">|</span><a title="慕和南道租房"  href="http://cd.lianjia.com/zufang/c3011055414228/" >22套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/tianfuxinqu/" class="district" title="天府新区小区">天府新区</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/huayang/" class="bizcircle" title="华阳小区">华阳</a>&nbsp;
                  /&nbsp;2010年建成
          </div>
        <div class="tagList">
                </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>11728</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="慕和南道二手房" href="http://cd.lianjia.com/ershoufang/c3011055414228/" class="totalSellCount"><span>21</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/1611041535394/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/0eb6b0f0-cd97-4196-8016-857f247e8b6f.jpg.232x174.jpg" alt="中海龙湾半岛">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/1611041535394/" target="_blank">中海龙湾半岛</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="中海龙湾半岛网签"  href="http://cd.lianjia.com/chengjiao/c1611041535394/" >90天成交16套</a>
      <span class="cutLine">|</span><a title="中海龙湾半岛租房"  href="http://cd.lianjia.com/zufang/c1611041535394/" >9套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/wuhou/" class="district" title="武侯小区">武侯</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/longwan/" class="bizcircle" title="龙湾小区">龙湾</a>&nbsp;
                  /&nbsp;2009年建成
          </div>
        <div class="tagList">
                </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>17229</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="中海龙湾半岛二手房" href="http://cd.lianjia.com/ershoufang/c1611041535394/" class="totalSellCount"><span>43</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/1611047199430/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/66ada28f-0e4a-4191-a0c1-b0928f6afe46.jpg.232x174.jpg" alt="南城都汇汇尚园">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/1611047199430/" target="_blank">南城都汇汇尚园</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="南城都汇汇尚园网签"  href="http://cd.lianjia.com/chengjiao/c1611047199430/" >90天成交13套</a>
      <span class="cutLine">|</span><a title="南城都汇汇尚园租房"  href="http://cd.lianjia.com/zufang/c1611047199430/" >31套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/gaoxin7/" class="district" title="高新小区">高新</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/shiyiyiyuan/" class="bizcircle" title="市一医院小区">市一医院</a>&nbsp;
                  /&nbsp;2014年建成
          </div>
        <div class="tagList">
                    <span>近地铁1号线高新站</span>
          </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>17361</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="南城都汇汇尚园二手房" href="http://cd.lianjia.com/ershoufang/c1611047199430/" class="totalSellCount"><span>21</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/1611047737374/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/c0d13e7f-8cab-46b6-8346-77b316966541.jpg.232x174.jpg" alt="中海兰庭">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/1611047737374/" target="_blank">中海兰庭</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="中海兰庭网签"  href="http://cd.lianjia.com/chengjiao/c1611047737374/" >90天成交16套</a>
      <span class="cutLine">|</span><a title="中海兰庭租房"  href="http://cd.lianjia.com/zufang/c1611047737374/" >24套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/gaoxin7/" class="district" title="高新小区">高新</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/dayuan/" class="bizcircle" title="大源小区">大源</a>&nbsp;
                  /&nbsp;2008年建成
          </div>
        <div class="tagList">
                </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>18871</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="中海兰庭二手房" href="http://cd.lianjia.com/ershoufang/c1611047737374/" class="totalSellCount"><span>29</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/3011055407060/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/68a6dcad-b6e9-4ac2-b72c-805ce3458a97.png.232x174.jpg" alt="金茂光明城市">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/3011055407060/" target="_blank">金茂光明城市</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="金茂光明城市网签"  href="http://cd.lianjia.com/chengjiao/c3011055407060/" >90天成交35套</a>
      <span class="cutLine">|</span><a title="金茂光明城市租房"  href="http://cd.lianjia.com/zufang/c3011055407060/" >46套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/tianfuxinqu/" class="district" title="天府新区小区">天府新区</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/huayang/" class="bizcircle" title="华阳小区">华阳</a>&nbsp;
                  /&nbsp;2016年建成
          </div>
        <div class="tagList">
                </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>13388</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="金茂光明城市二手房" href="http://cd.lianjia.com/ershoufang/c3011055407060/" class="totalSellCount"><span>37</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/3011056066692/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/8ec47835-c3d5-48a2-ae74-6096b6f8a540.jpg.232x174.jpg" alt="恒大天府半岛1期">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/3011056066692/" target="_blank">恒大天府半岛1期</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="恒大天府半岛1期网签"  href="http://cd.lianjia.com/chengjiao/c3011056066692/" >90天成交30套</a>
      <span class="cutLine">|</span><a title="恒大天府半岛1期租房"  href="http://cd.lianjia.com/zufang/c3011056066692/" >1套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/tianfuxinqu/" class="district" title="天府新区小区">天府新区</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/nanhu/" class="bizcircle" title="南湖小区">南湖</a>&nbsp;
                  /&nbsp;2010年建成
          </div>
        <div class="tagList">
                </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>11485</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="恒大天府半岛1期二手房" href="http://cd.lianjia.com/ershoufang/c3011056066692/" class="totalSellCount"><span>10</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/3011055400648/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/1c7cf494-5890-423a-945e-dcc3f055ee59.jpg.232x174.jpg" alt="英郡三期">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/3011055400648/" target="_blank">英郡三期</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="英郡三期网签"  href="http://cd.lianjia.com/chengjiao/c3011055400648/" >90天成交15套</a>
      <span class="cutLine">|</span><a title="英郡三期租房"  href="http://cd.lianjia.com/zufang/c3011055400648/" >25套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/gaoxin7/" class="district" title="高新小区">高新</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/xinhuizhan/" class="bizcircle" title="新会展小区">新会展</a>&nbsp;
                  /&nbsp;2012年建成
          </div>
        <div class="tagList">
                    <span>近地铁1号线世纪城站</span>
          </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>14481</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="英郡三期二手房" href="http://cd.lianjia.com/ershoufang/c3011055400648/" class="totalSellCount"><span>22</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/3011055412135/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/f4fa92a6-cb39-4e61-a8bd-7c457c1a8e0e.jpg.232x174.jpg" alt="华润凤凰城一期">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/3011055412135/" target="_blank">华润凤凰城一期</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="华润凤凰城一期网签"  href="http://cd.lianjia.com/chengjiao/c3011055412135/" >90天成交14套</a>
      <span class="cutLine">|</span><a title="华润凤凰城一期租房"  href="http://cd.lianjia.com/zufang/c3011055412135/" >15套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/gaoxin7/" class="district" title="高新小区">高新</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/dayuan/" class="bizcircle" title="大源小区">大源</a>&nbsp;
                  /&nbsp;2013年建成
          </div>
        <div class="tagList">
                </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>19711</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="华润凤凰城一期二手房" href="http://cd.lianjia.com/ershoufang/c3011055412135/" class="totalSellCount"><span>35</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/3011056066488/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/a5b73af7-7803-4cb2-a0d7-99be675e37bb.jpg.232x174.jpg" alt="佳兆业君汇上品">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/3011056066488/" target="_blank">佳兆业君汇上品</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="佳兆业君汇上品网签"  href="http://cd.lianjia.com/chengjiao/c3011056066488/" >90天成交35套</a>
      <span class="cutLine">|</span><a title="佳兆业君汇上品租房"  href="http://cd.lianjia.com/zufang/c3011056066488/" >5套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/tianfuxinqu/" class="district" title="天府新区小区">天府新区</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/nanhu/" class="bizcircle" title="南湖小区">南湖</a>&nbsp;
                  /&nbsp;2013年建成
          </div>
        <div class="tagList">
                </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>10750</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="佳兆业君汇上品二手房" href="http://cd.lianjia.com/ershoufang/c3011056066488/" class="totalSellCount"><span>25</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/1611041465350/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/c17c9fc1-e163-41fe-8145-f41961b5ca71.jpg.232x174.jpg" alt="上锦雅筑">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/1611041465350/" target="_blank">上锦雅筑</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="上锦雅筑网签"  href="http://cd.lianjia.com/chengjiao/c1611041465350/" >90天成交17套</a>
      <span class="cutLine">|</span><a title="上锦雅筑租房"  href="http://cd.lianjia.com/zufang/c1611041465350/" >16套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/wuhou/" class="district" title="武侯小区">武侯</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/tongzilin/" class="bizcircle" title="桐梓林小区">桐梓林</a>&nbsp;
                  /&nbsp;2006年建成
          </div>
        <div class="tagList">
                    <span>近地铁1号线桐梓林站</span>
          </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>10184</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="上锦雅筑二手房" href="http://cd.lianjia.com/ershoufang/c1611041465350/" class="totalSellCount"><span>8</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/1611043161440/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/2603b130-becd-4162-b862-faf272d4d85b.jpg.232x174.jpg" alt="优品道一、二期">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/1611043161440/" target="_blank">优品道一、二期</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="优品道一、二期网签"  href="http://cd.lianjia.com/chengjiao/c1611043161440/" >90天成交2套</a>
      <span class="cutLine">|</span><a title="优品道一、二期租房"  href="http://cd.lianjia.com/zufang/c1611043161440/" >1套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/qingyang/" class="district" title="青羊小区">青羊</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/youpindao/" class="bizcircle" title="优品道小区">优品道</a>&nbsp;
                  /&nbsp;2010年建成
          </div>
        <div class="tagList">
                    <span>近地铁4号线文化宫站</span>
          </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>16830</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="优品道一、二期二手房" href="http://cd.lianjia.com/ershoufang/c1611043161440/" class="totalSellCount"><span>5</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/1611043156602/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/771c6024-78af-4f64-99e2-02077a832696.JPG.232x174.jpg" alt="博瑞都市花园">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/1611043156602/" target="_blank">博瑞都市花园</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="博瑞都市花园网签"  href="http://cd.lianjia.com/chengjiao/c1611043156602/" >90天成交9套</a>
      <span class="cutLine">|</span><a title="博瑞都市花园租房"  href="http://cd.lianjia.com/zufang/c1611043156602/" >7套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/qingyang/" class="district" title="青羊小区">青羊</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/youpindao/" class="bizcircle" title="优品道小区">优品道</a>&nbsp;
                  /&nbsp;2002年建成
          </div>
        <div class="tagList">
                    <span>近地铁4号线文化宫站</span>
          </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>15643</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="博瑞都市花园二手房" href="http://cd.lianjia.com/ershoufang/c1611043156602/" class="totalSellCount"><span>6</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/3011055110938/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/0c0a6d21-568a-46de-ba45-93f8f8f28613.jpg.232x174.jpg" alt="华润二十四城二期">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/3011055110938/" target="_blank">华润二十四城二期</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="华润二十四城二期网签"  href="http://cd.lianjia.com/chengjiao/c3011055110938/" >90天成交21套</a>
      <span class="cutLine">|</span><a title="华润二十四城二期租房"  href="http://cd.lianjia.com/zufang/c3011055110938/" >18套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/chenghua/" class="district" title="成华小区">成华</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/wanxiangcheng1/" class="bizcircle" title="万象城小区">万象城</a>&nbsp;
                  /&nbsp;2010年建成
          </div>
        <div class="tagList">
                    <span>近地铁4号线万年场站</span>
          </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>18516</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="华润二十四城二期二手房" href="http://cd.lianjia.com/ershoufang/c3011055110938/" class="totalSellCount"><span>22</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/3011055361769/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/3e6725cb-a849-4f84-811a-8d63d3fbbf09.jpg.232x174.jpg" alt="派克公馆">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/3011055361769/" target="_blank">派克公馆</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="派克公馆网签"  href="http://cd.lianjia.com/chengjiao/c3011055361769/" >90天成交97套</a>
      <span class="cutLine">|</span><a title="派克公馆租房"  href="http://cd.lianjia.com/zufang/c3011055361769/" >26套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/pidou/" class="district" title="郫都小区">郫都</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/chengwai/" class="bizcircle" title="成外小区">成外</a>&nbsp;
                  /&nbsp;2007年建成
          </div>
        <div class="tagList">
                    <span>近地铁2号线金周路站</span>
          </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>7897</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="派克公馆二手房" href="http://cd.lianjia.com/ershoufang/c3011055361769/" class="totalSellCount"><span>68</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/1611049015431/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/de5a4952-2752-4493-a1a3-1ab5be5e08ef.jpg.232x174.jpg" alt="中海城南华府">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/1611049015431/" target="_blank">中海城南华府</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="中海城南华府网签"  href="http://cd.lianjia.com/chengjiao/c1611049015431/" >90天成交5套</a>
      <span class="cutLine">|</span><a title="中海城南华府租房"  href="http://cd.lianjia.com/zufang/c1611049015431/" >26套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/gaoxin7/" class="district" title="高新小区">高新</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/jinrongcheng/" class="bizcircle" title="金融城小区">金融城</a>&nbsp;
                  /&nbsp;2013年建成
          </div>
        <div class="tagList">
                    <span>近地铁1号线金融城站</span>
          </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>28606</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="中海城南华府二手房" href="http://cd.lianjia.com/ershoufang/c1611049015431/" class="totalSellCount"><span>23</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/3011052818943/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/60f9c9b4-53a9-44d5-b6fe-a6b300473192.jpg.232x174.jpg" alt="蓝光圣菲town城">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/3011052818943/" target="_blank">蓝光圣菲town城</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="蓝光圣菲town城网签"  href="http://cd.lianjia.com/chengjiao/c3011052818943/" >90天成交40套</a>
      <span class="cutLine">|</span><a title="蓝光圣菲town城租房"  href="http://cd.lianjia.com/zufang/c3011052818943/" >10套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/shuangliu/" class="district" title="双流小区">双流</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/hangkonggang/" class="bizcircle" title="航空港小区">航空港</a>&nbsp;
                  /&nbsp;2009年建成
          </div>
        <div class="tagList">
                </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>8713</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="蓝光圣菲town城二手房" href="http://cd.lianjia.com/ershoufang/c3011052818943/" class="totalSellCount"><span>30</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/1611041555455/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/6832b8b9-fb9d-476e-bcfc-858c10196736.jpg.232x174.jpg" alt="中铁西子香荷">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/1611041555455/" target="_blank">中铁西子香荷</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="中铁西子香荷网签"  href="http://cd.lianjia.com/chengjiao/c1611041555455/" >90天成交13套</a>
      <span class="cutLine">|</span><a title="中铁西子香荷租房"  href="http://cd.lianjia.com/zufang/c1611041555455/" >18套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/qingyang/" class="district" title="青羊小区">青羊</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/guanghuapaoxiao/" class="bizcircle" title="光华泡小小区">光华泡小</a>&nbsp;
                  /&nbsp;2010年建成
          </div>
        <div class="tagList">
                </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>18266</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="中铁西子香荷二手房" href="http://cd.lianjia.com/ershoufang/c1611041555455/" class="totalSellCount"><span>20</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
<li class="clear xiaoquListItem">
  <a class="img" href="http://cd.lianjia.com/xiaoqu/1611058892595/" target="_blank" rel="nofollow">
    <img class="lj-lazy" src="http://s1.ljcdn.com/feroot/pc/asset/img/blank.gif?_v=20170317185744" data-original="http://image1.ljcdn.com/hdic-resblock/f62c47c8-73ca-4daa-a869-9dd2e677ab6c.JPG.232x174.jpg" alt="万科海悦汇城西区">
  </a>
  <div class="info">
    <div class="title">
      <a href="http://cd.lianjia.com/xiaoqu/1611058892595/" target="_blank">万科海悦汇城西区</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="万科海悦汇城西区网签"  href="http://cd.lianjia.com/chengjiao/c1611058892595/" >90天成交45套</a>
      <span class="cutLine">|</span><a title="万科海悦汇城西区租房"  href="http://cd.lianjia.com/zufang/c1611058892595/" >7套正在出租</a>
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="http://cd.lianjia.com/xiaoqu/tianfuxinqu/" class="district" title="天府新区小区">天府新区</a>
      &nbsp;<a href="http://cd.lianjia.com/xiaoqu/haiyanggongyuan/" class="bizcircle" title="海洋公园小区">海洋公园</a>&nbsp;
                  /&nbsp;2012年建成
          </div>
        <div class="tagList">
                </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>13662</span>元/m<sup>2</sup></div>
            <div class="priceDesc">2月二手房参考均价</div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="万科海悦汇城西区二手房" href="http://cd.lianjia.com/ershoufang/c1611058892595/" class="totalSellCount"><span>23</span>套</a>
      <div class="sellCountDesc">在售二手房</div>
    </div>
      </div>
</li>
</ul><!-- 无搜索结果 --><div class="contentBottom clear" ><div class="crumbs fl"><a href="/">链家网成都站</a><span >&nbsp;&gt;&nbsp;</span><h1><a href="/xiaoqu/">成都小区</a></h1></div><div class="page-box fr"><div class="page-box house-lst-page-box" comp-module='page' page-url="/xiaoqu/pg{page}/"page-data='{"totalPage":100,"curPage":1}'></div>


</div></div><div style="display:none;"><p>成都小区信息</p><p>链家网成都站成都小区频道提供真实、时时的成都小区房源信息，成都小区目前为9574个，全>部由线下经纪人确认核实上传，信息可靠，成都小区用户可以在链家网成都小区频道和成都小区频道移动端最快速、最及时的找到自己想要的真>实、放心房源。链家网成都小区平台，真房源，如你所见！</p><p>小区均价:9631.4,建成年代:2001,物业费用:1,开发商:四川大行宏业房地产开发有限公司,物业公司:四川锦宏家族物业管理有限公司,楼栋总数:3,容积率:2.9,房屋总数:659,绿化率:33,小区均价:7592.18,建成年代:2009,物业费用:1.98,开发商:四川炎华置信实业（集团）有限公司,物业公司:成都洁华物业管理有限公司,楼栋总数:13,容积率:3.6,房屋总数:2324,绿化率:30</p></div></div><!-- 右侧sidebar --><div class="rightContent">
<div class="sideBar_price" id='priceSideBarContainer'></div>
<div class="sideBar_hotResblock" id="hotResblockContainer">
  <div class="hotResblockTitle">北京热门小区</div>
  <ul>
  </ul>
  <a class="moreResblock_sidebar">查看更多热门小区&nbsp;>></a>
</div>
<div class="sideBar_ADSuggest" id="ADSuggestContainer"></div>
<div class="sideBar_zixun sideBar_wenda" id="pushZixunContainer"></div>
<div class="sideBar_wenda" id="pushWendaContainer"></div>

<script type="text/template" id="priceSideBarTpl">
<%if(tag !== 'school'){%>
  <div class="title"><%=name%>最新参考均价</div>
  <div class="priceMap" id="priceChartContainer"></div>
  <a href="<%=fangjia_url%>" class="unitPrice" target="_blank">
    <span><%=month_trans%></span>元/平米
  </a>
  <div class="info">
    <a href="<%=fangjia_url%>" target="_blank">环比上月均价<%=month_trans_ratio>=0?'上涨':'下降'%> <%=month_trans_ratio%>%</a>
    <a href="<%=chengjiao_url%>" target="_blank">/ 近90天成交<%=sold_90_day%>套</a>
    <%if(tag === '小区'){%>
    <div>
      <a class="cardMoreDetail" href="<%=url%>" target="_blank">查看小区详情>></a>
    </div>
    <%}%>
  </div>
<%}else{%>
  <a class="title" href="<%=url%>" target="_blank"><%=name%></a>
  <div class="unitPrice school">
    <span><%=min_unit_price%></span>万元起
  </div>
  <div class="info">
    <a href="<%=url%>" target="_blank">本学区目前有在售二手房<%=sell_num%>套，划片小区<%=resblock_nums%>个</a>
    <a class="cardMoreDetail" href="<%=url%>"  target="_blank">查看学区详情>></a>
  </div>
<%}%>
</script>

<script type="text/tempalte" id="hotResblockTpl">
  <div class="hotResblockTitle"><%=name%>成交量排行</div>
  <ul>
  <%for(var i = 0; i < rank.length; i++){%>
    <li class="clear">
    <%if(i < 3){%>
      <div class="num top"><%=i+1%></div>
    <%}else{%>
      <div class="num"><%=i+1%></div>
    <%}%>
      <a href="<%=rank[i].url%>" class="resblockName_sidebar" title="<%=rank[i].resblock_name%>"><%=rank[i].resblock_name%></a>
      <div class="reblockPrice_sidebar"><%=Math.round(rank[i].trans_price)%>元/㎡</div>
    </li>
  <%}%>
  </ul>
  <a href="<%=url%>" class="moreResblock_sidebar">查看更多小区成交量&nbsp;>></a>
</script>
<script type="text/template" id="pushWendaTpl">
  <div class="title">热门问答</div>
  <ul>
  <%for(var i = 0;i < list.length; i++){%>
    <li>
      <a class="info" href="<%=list[i].url%>" target="_blank" data-bl="list" data-log_index="<%=i+1%>"><%=list[i].question_title%></a>
      <span class="time"><%=list[i].mtime%></span>
    </li>
  <%}%>
  </ul>
</script>
<script type="text/template" id="pushZixunTpl">
  <div class="title">热点精选</div>
  <ul>
  <%for(var i = 0;i < list.length; i++){%>
    <li>
      <a class="info" href="<%=list[i].url%>" target="_blank" data-bl="list" data-log_index="<%=i+1%>">
        <i class="opt<%=i%>"><%=i+1%></i>
        <span><%=list[i].question_title%></span>
      </a>
    </li>
  <%}%>
  </ul>
</script>
<script type="text/template" id="sideBar_ADSuggest_tpl">
  <a class="img" href="<%=url%>" target="_blank" data-bl="list" data-log_index="<%=index+1%>">
    <img src="<%=img_url%>" alt="">
    <div class="cover"></div>
    <div class="title">
      <span><%=title%></span>&nbsp;
    </div>
  </a>
  <div class="pointContainer">
  <%for(var i = 0; i < total; i++){%>
    <%if(index === i){%>
      <span data-index="<%=i%>" class="point selected"></span>
    <%}else{%>
      <span data-index="<%=i%>" class="point"></span>
    <%}%>
  <%}%>
  </div>
</script>
</div></div><div class="footer"><div class="wrapper"><div class="f-title"><div class="fl"><ul><li><a href="http://www.lianjia.com/zhuanti/home/" target="_blank">了解链家网</a></li><li><a href="http://cd.lianjia.com/about/aboutlianjia/" rel="nofollow" target="_blank">关于链家</a></li><li><a href="http://cd.lianjia.com/about/contactus/" rel="nofollow" target="_blank">联系我们</a></li><li><a href="http://join.lianjia.com/" rel="nofollow" target="_blank">加入我们</a></li><li><a href="http://www.lianjia.com/privacy/" rel="nofollow" target="_blank">隐私声明</a></li><li><a href="http://cd.lianjia.com/sitemap/" target="_blank">网站地图</a></li><li><a href="http://www.lianjia.com/notice/7.html" target="_blank">友情链接</a></li><li><a href="http://agent.lianjia.com/" rel="nofollow" target="_blank">经纪人登录</a></li></ul></div><div class="fr">官方客服 1010 9666</div></div><div class="lianjia-link-box"><div class="fl"><div class="tab"><span  class="hover">热门城市小区</span><span >热门城市二手房</span><span >热门城市租房网</span><span >热门城市楼盘</span><span >热门百科</span><span >合作与友情链接</span></div><div class="link-list"><div><dd><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611041516890/">凯莱国际寓所二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611061253243/">南阳锦城晶品二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c3011053919910/">龙门镇二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c3011053573846/">沙河壹号一期二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c3011055385914/">红树湾二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611041522684/">银唐国际二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611041554183/">优客联邦一期二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611058922197/">蓝光时代华章二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c3011053977876/">龙门镇二期二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611058981572/">左岸花都二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611043102650/">凯丽滨江花园二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611041737871/">喜年广场A栋二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c3011053459346/">康郡二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611048090474/">御都花园别墅二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611041574805/">碧华邻二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611041812010/">御府花都二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611041500168/">花间集二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611048572622/">布鲁明顿广场二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611041579253/">齐力碧水湾二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611044060273/">优客联邦三期二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611043451443/">保利金香槟二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611041510720/">都会风尚二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611048245025/">首航欣程二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611043135126/">交大归谷国际社区二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611061083009/">绿水康城二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611047922039/">华韵天府二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611060460905/">原乡二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611043042770/">锦绣花园西区二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c1611043056243/">上海花园二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/c168141017459951/">雅居乐花园峰会北区二手房</a></dd></div><div><dd><a target="_blank" href="http://bj.lianjia.com/ershoufang/">北京二手房</a><a target="_blank" href="http://gz.lianjia.com/ershoufang/">广州二手房</a><a target="_blank" href="http://sz.lianjia.com/ershoufang/">深圳二手房</a><a target="_blank" href="http://tj.lianjia.com/ershoufang/">天津二手房</a><a target="_blank" href="http://cd.lianjia.com/ershoufang/">成都二手房</a><a target="_blank" href="http://nj.lianjia.com/ershoufang/">南京二手房</a><a target="_blank" href="http://hz.lianjia.com/ershoufang/">杭州二手房</a><a target="_blank" href="http://qd.lianjia.com/ershoufang/">青岛二手房</a><a target="_blank" href="http://dl.lianjia.com/ershoufang/">大连二手房</a><a target="_blank" href="http://xm.lianjia.com/ershoufang/">厦门二手房</a><a target="_blank" href="http://wh.lianjia.com/ershoufang/">武汉二手房</a><a target="_blank" href="http://cq.lianjia.com/ershoufang/">重庆二手房</a><a target="_blank" href="http://cs.lianjia.com/ershoufang/">长沙二手房</a><a target="_blank" href="http://jn.lianjia.com/ershoufang/">济南二手房</a><a target="_blank" href="http://fs.lianjia.com/ershoufang/">佛山二手房</a></dd></div><div><dd><a target="_blank" href="http://bj.lianjia.com/zufang/">北京租房</a><a target="_blank" href="http://gz.lianjia.com/zufang/">广州租房</a><a target="_blank" href="http://sz.lianjia.com/zufang/">深圳租房</a><a target="_blank" href="http://tj.lianjia.com/zufang/">天津租房</a><a target="_blank" href="http://cd.lianjia.com/zufang/">成都租房</a><a target="_blank" href="http://nj.lianjia.com/zufang/">南京租房</a><a target="_blank" href="http://hz.lianjia.com/zufang/">杭州租房</a><a target="_blank" href="http://qd.lianjia.com/zufang/">青岛租房</a><a target="_blank" href="http://dl.lianjia.com/zufang/">大连租房</a><a target="_blank" href="http://xm.lianjia.com/zufang/">厦门租房</a><a target="_blank" href="http://wh.lianjia.com/zufang/">武汉租房</a><a target="_blank" href="http://cq.lianjia.com/zufang/">重庆租房</a><a target="_blank" href="http://cs.lianjia.com/zufang/">长沙租房</a><a target="_blank" href="http://jn.lianjia.com/zufang/">济南租房</a></dd></div><div><dd><a target="_blank" href="http://sh.fang.lianjia.com/">北京楼盘</a><a target="_blank" href="http://tj.fang.lianjia.com/">天津楼盘</a><a target="_blank" href="http://nj.fang.lianjia.com/">南京楼盘</a><a target="_blank" href="http://cd.fang.lianjia.com/">成都楼盘</a><a target="_blank" href="http://dl.fang.lianjia.com/">大连楼盘</a><a target="_blank" href="http://qd.fang.lianjia.com/">青岛楼盘</a><a target="_blank" href="http://hz.fang.lianjia.com/">杭州楼盘</a><a target="_blank" href="http://wh.fang.lianjia.com/">武汉楼盘</a><a target="_blank" href="http://sz.fang.lianjia.com/">深圳楼盘</a><a target="_blank" href="http://cq.fang.lianjia.com/">重庆楼盘</a><a target="_blank" href="http://cs.fang.lianjia.com/">长沙楼盘</a><a target="_blank" href="http://xa.fang.lianjia.com/">西安楼盘</a><a target="_blank" href="http://jn.fang.lianjia.com/">济南楼盘</a><a target="_blank" href="http://sjz.fang.lianjia.com/">石家庄楼盘</a></dd></div><div><dd><a target="_blank" href="http://news.cd.lianjia.com/baike/011207.html">绿地率和绿化率对比</a><a target="_blank" href="http://news.cd.lianjia.com/baike/010664.html">买卖小产权房风险</a><a target="_blank" href="http://news.cd.lianjia.com/baike/010530.html">房屋产权核验要素</a><a target="_blank" href="http://news.bj.lianjia.com/baike/033371.html">如何选择换房方案</a><a target="_blank" href="http://news.bj.lianjia.com/baike/06645.html">卖房收款项</a><a target="_blank" href="http://news.bj.lianjia.com/baike/029526.html">买两限房注意事项</a><a target="_blank" href="http://news.bj.lianjia.com/baike/017029.html">卖房补充协议</a><a target="_blank" href="http://news.bj.lianjia.com/baike/027738.html">租房物业交割</a><a target="_blank" href="http://news.bj.lianjia.com/baike/019792.html">二手房资金监管</a><a target="_blank" href="http://news.bj.lianjia.com/baike/017745.html">通州二手房限购政策</a><a target="_blank" href="http://news.bj.lianjia.com/baike/06607.html">新房装修注意事项</a><a target="_blank" href="http://news.dl.lianjia.com/baike/09536.html">大连购房奖励领取</a><a target="_blank" href="http://news.dl.lianjia.com/baike/06682.html">买房公证类型</a><a target="_blank" href="http://news.dl.lianjia.com/baike/025723.html">房屋法定继承顺序</a><a target="_blank" href="http://news.dl.lianjia.com/baike/030230.html">大连购房提取公积金</a><a target="_blank" href="http://news.dl.lianjia.com/baike/09438.html">大连二手房购买流程</a><a target="_blank" href="http://news.dl.lianjia.com/baike/049312.html">二手房个人所得税</a><a target="_blank" href="http://news.dl.lianjia.com/baike/054567.html">新房得房率计算</a><a target="_blank" href="http://news.dl.lianjia.com/baike/032782.html">商业贷款银行拒贷</a><a target="_blank" href="http://news.dl.lianjia.com/baike/052395.html">大连买房落户</a><a target="_blank" href="http://news.tj.lianjia.com/baike/010503.html">买新房二手房区别</a><a target="_blank" href="http://news.tj.lianjia.com/baike/010865.html">二手房买卖交易流程</a><a target="_blank" href="http://news.tj.lianjia.com/baike/09968.html">物业交割清算费用</a><a target="_blank" href="http://news.tj.lianjia.com/baike/017136.html">二手房交定金注意事项</a><a target="_blank" href="http://news.tj.lianjia.com/baike/011251.html">二手房遗留物业费</a><a target="_blank" href="http://news.tj.lianjia.com/baike/011420.html">二手房物业交割步骤</a><a target="_blank" href="http://news.sjz.lianjia.com/baike/0102291.html">规避租房合同纠纷</a><a target="_blank" href="http://news.sjz.lianjia.com/baike/099896.html">农村房产买卖政策</a><a target="_blank" href="http://news.sjz.lianjia.com/baike/099157.html">套内建筑面积</a><a target="_blank" href="http://news.sjz.lianjia.com/baike/098358.html">规避查房封房风险</a><a target="_blank" href="http://news.sjz.lianjia.com/baike/098105.html">老房子采光改造</a><a target="_blank" href="http://news.sjz.lianjia.com/baike/097456.html">好户型实例解析</a><a target="_blank" href="http://news.sjz.lianjia.com/baike/030648.html">委托买房核实真假</a><a target="_blank" href="http://news.sjz.lianjia.com/baike/038797.html">委托中介买房环节</a><a target="_blank" href="http://news.sjz.lianjia.com/baike/033364.html">购房意向定金退还</a><a target="_blank" href="http://news.sjz.lianjia.com/baike/033385.html">买安置房风险</a><a target="_blank" href="http://news.sjz.lianjia.com/baike/018776.html">石家庄住房公积金提取</a><a target="_blank" href="http://news.sjz.lianjia.com/baike/08331.html">办理房产继承公证</a><a target="_blank" href="http://news.cd.lianjia.com/baike/040041.html">小户型的装修技巧</a><a target="_blank" href="http://news.sjz.lianjia.com/baike/098088.html">水路验收标准</a></dd></div><div><dd><a target="_blank" href="http://www.xhj.com/xiaoqu/">长沙小区</a><a target="_blank" href="http://www.lianjia.com/">房产网</a><a target="_blank" href="http://m.lianjia.com/cd/">手机成都房产网</a></dd></div></div></div><div class="clear"></div></div><div class="bottom"><div class="copyright fl">北京链家房地产经纪有限公司 | 网络经营许可证 京ICP备11024601号-12 | © Copyright©2010-2017 链家网Lianjia.com版权所有</div></div></div></div>

<script src="http://s1.ljcdn.com/feroot/pc/asset/base/fe.js?_v=20170317185744"></script><script src="http://s1.ljcdn.com/feroot/pc/asset/common/common.js?_v=20170317185744"></script><div style="display:none"><script src="http://s1.ljcdn.com/feroot/dep/ljanalytics.js?_v=20170317185744"></script></div><div id="only" data-city="cd" data-page="xiaoqu_list"></div>
<script>var path = 'http://s1.ljcdn.com/feroot/pc/asset?_v=20170317185744'.split("?");require.config({baseUrl: path[0],paths: {'echarts' : '../../dep/echarts-1.4.1/build/echarts','echarts/chart/bar' : '../../dep/echarts-1.4.1/build/echarts','echarts/chart/line' : '../../dep/echarts-1.4.1/build/echarts','echarts/chart/pie' : '../../dep/echarts-1.4.1/build/echarts','echarts3' : '../../dep/echarts3/echarts3','common': 'common','jquery-ui': '../../dep/jquery-ui/jquery-ui.min','zeroclipboard': '../../dep/zeroclipboard-2.2.0/ZeroClipboard'},urlArgs:  path[1]});var feData = {"cityName": "北京","getFavHouseUrl":       "/api/gethousefav","setFavHouseUrl":       "/api/sethousefav","getLastSearch":        "/api/getlastsearch","getCommunityHistory":  "/api/getcommunityhistory","verifyHouse":          "/api/verifyHouse","getUser":              "/api/getUser","verifyCode":           "/api/getVerifyCode","complaint":            "/api/complaint","getDecoration":        "/api/getDecoration","trendData" :           "/site/getpicinfo"}</script>

<script type="text/javascript">
require(['ershoufang/xiaoquList/index'], function (main) {
  main({
    sidebar:{"type":"city","cityId":510100,"uuid":"dbec72f5-1878-4f38-b1bb-cad25817ae6b","ucid":null,"id":510100}
  });
});
require(['common/backtopV3'], function (main) {
  main({
    ucid: '',
    uuid: 'dbec72f5-1878-4f38-b1bb-cad25817ae6b',
    loadingImg: 'http://s1.ljcdn.com/feroot/pc/asset/ershoufang/sellDetail/img/loading.gif?_v=20170317185744',
    qrImg: 'http://s1.ljcdn.com/feroot/pc/asset/img/home/sidebar_qr.png?_v=20170317185744'
  });
});
</script>
<script>require(['common/suggestion'], function (suggestion) {window.defaultSuggest = suggestion.init({requestOptions: {cityId: '510100',cityName: '成都'},url: '/api/headerSearch?channel=xiaoqu&q=',main: '#keyword-box',appendTo: '#suggest-cont',redirect: true});});</script><div class="loninContaner"><div class="overlay_bg"></div><div class="panel_login animated" id="dialog"><div class="panel_info"><div class="panel_tab"><div class="title"><div class="fl">用户登录</div><label class="fr">还没有链家网账号？<a href="//passport.lianjia.com/register/resources/lianjia/register.html?service=http%3A%2F%2Fbj.lianjia.com%2F">马上注册</a></label></div><div class="clear"></div><div id="con_login_user"><form action="" method="post"><ul><li class="show-error"><dd>用户名或密码错误</dd></li><li class="item userName"><i></i><input type="text" class="the_input users" placeholder="请输入手机号" /></li><li class="item pwd"><i></i><input type="password" class="the_input password"  placeholder="请输入登录密码"/></li><li class="item checkVerimg" style="display:none;"><i></i><input type="text" class="the_input ver-img" maxlength="4"  placeholder="请输入验证码"/><img class="verImg"></li><li class="li_01"><label><input type="checkbox" name="remember" value="1" class="mind-login" checked>下次自动登录</label><a href="https://passport.lianjia.com/register/resources/lianjia/forget.html?service=http://bj.lianjia.com/">找回密码</a></li><li><a class="login-user-btn"  />立即登录</a></li></ul></form></div><div id="con_login_agent" class="undis"><form action="" method="post"><ul><li class="item"><dd></dd><input type="text" class="the_input users" placeholder="输入经纪人ID号码" /></li><li class="item"><input type="password" class="the_input password"  placeholder="登录密码"/></li><li class="li_01"><label><input type="checkbox" name="remember" value="1" class="mind-login">下次自动登录</label><a href="https://passport.lianjia.com/register/resources/lianjia/forget.html?service=http://bj.lianjia.com/">找回密码</a></li><li><input class="login-agent-btn" value="立即登录"/></li></ul></form></div></div></div><div class="registered"></div></div></div><!-- LianjiaIM Style --><link property='stylesheet' rel="stylesheet" href="http://s1.ljcdn.com/feroot/pc/asset/lianjiaIM/css/lianjiaim.css?_v=20170317185744"/><script src="//s1.ljcdn.com/web-im-sdk/static/0.9/ljim-core.min.js?_v=20170320"></script><script>(function() {var imConf = {"ajaxroot":"\/\/ajax.api.lianjia.com\/","imAppid":"LIANJIA_WEB_20160624","imAppkey":"6dfdcee27d78b1107fceeca55d80b7bd"};$.listener.on('userInfo', function (data) {if (data.code === 1) {data.ucid = '';}require(['lianjiaIM/lianjiaim'], function (LianjiaIM) {var ljim = new LianjiaIM({appid: imConf.imAppid,appkey: imConf.imAppkey,userData: data,staticRoot: 'http://s1.ljcdn.com/feroot/?_v=20170317185744'});});});})();</script><script type="text/javascript">var advert = 'http://s1.ljcdn.com/feroot/pc/asset/common/advert.js?_v=20170317185744';
    $.listener.on('userInfo', function (data) {
      window.loginData = data;
    });
    var mvl = document.createElement('script');
    mvl.type = 'text/javascript';
    mvl.async = true;
    mvl.src = advert;
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(mvl, s);
  </script><script type="text/javascript">(function(){var bp = document.createElement('script');var curProtocol = window.location.protocol.split(':')[0];if (curProtocol === 'https'){bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';} else {bp.src = 'http://push.zhanzhang.baidu.com/push.js';}var s = document.getElementsByTagName("script")[0];s.parentNode.insertBefore(bp, s);})();</script></body></html>

'''
