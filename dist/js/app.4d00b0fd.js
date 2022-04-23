(function(e){function t(t){for(var r,o,s=t[0],c=t[1],u=t[2],d=0,p=[];d<s.length;d++)o=s[d],Object.prototype.hasOwnProperty.call(i,o)&&i[o]&&p.push(i[o][0]),i[o]=0;for(r in c)Object.prototype.hasOwnProperty.call(c,r)&&(e[r]=c[r]);l&&l(t);while(p.length)p.shift()();return a.push.apply(a,u||[]),n()}function n(){for(var e,t=0;t<a.length;t++){for(var n=a[t],r=!0,s=1;s<n.length;s++){var c=n[s];0!==i[c]&&(r=!1)}r&&(a.splice(t--,1),e=o(o.s=n[0]))}return e}var r={},i={app:0},a=[];function o(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,o),n.l=!0,n.exports}o.m=e,o.c=r,o.d=function(e,t,n){o.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},o.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},o.t=function(e,t){if(1&t&&(e=o(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(o.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)o.d(n,r,function(t){return e[t]}.bind(null,r));return n},o.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return o.d(t,"a",t),t},o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},o.p="/";var s=window["webpackJsonp"]=window["webpackJsonp"]||[],c=s.push.bind(s);s.push=t,s=s.slice();for(var u=0;u<s.length;u++)t(s[u]);var l=c;a.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"034f":function(e,t,n){"use strict";n("85ec")},"56d7":function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var r=n("2b0e"),i=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"app"}},[n("div",[n("Scatterplot",{attrs:{id:"comp1",data:e.points,selection:[],encoding:{x:"West-East",y:"North-South"}},on:{brush:e.onBrush}})],1)])},a=[],o=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("Base",[n("div",{attrs:{id:e.id}})])},s=[],c=(n("4de4"),n("d3b7"),n("ddb0"),n("96cf"),n("2ef0")),u=n.n(c),l=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"base-comp"},[n("div",{staticClass:"center"},[e._t("default")],2)])},d=[],p={},f=p,h=(n("6a75"),n("2877")),v=Object(h["a"])(f,l,d,!1,null,null,null),g=v.exports,y=n("87e7"),m={data:function(){return{view:null}},computed:{vegaSpec:function(){return{data:{values:this.data},selection:{brush:{type:"interval"},multi:{type:"multi"}},mark:"point",encoding:{x:{field:this.encoding.x,type:"quantitative",scale:{domain:[0,10]}},y:{field:this.encoding.y,type:"quantitative",scale:{domain:[0,10]}},color:{condition:{selection:"brush",value:"blue"},value:"grey"},size:{value:50}},width:400,height:400}}},props:["id","data","selection","encoding"],watch:{vegaSpec:function(e){return regeneratorRuntime.async((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,regeneratorRuntime.awrap(this.embedVegaSpec(this.value));case 2:case"end":return e.stop()}}),null,this)},selection:function(e){var t;if(0===e.length)t=[[0,0],[0,0]];else{var n=u.a.minBy(e,this.encoding.x)[this.encoding.x],r=u.a.maxBy(e,this.encoding.x)[this.encoding.x],i=u.a.minBy(e,this.encoding.y)[this.encoding.y],a=u.a.maxBy(e,this.encoding.y)[this.encoding.y];t=[[n,r],[a,i]]}this.view.data("brush_store",[{fields:[{channel:"x",field:this.encoding.x,type:"R"},{channel:"y",field:this.encoding.y,type:"R"}],unit:"",values:t}]),this.view.runAsync()}},mounted:function(){return regeneratorRuntime.async((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,regeneratorRuntime.awrap(this.embedVegaSpec(this.vegaSpec));case 2:case"end":return e.stop()}}),null,this)},methods:{embedVegaSpec:function(e){var t,n=this;return regeneratorRuntime.async((function(r){while(1)switch(r.prev=r.next){case 0:return r.next=2,regeneratorRuntime.awrap(Object(y["a"])("#".concat(this.id),e,{renderer:"svg"}));case 2:t=r.sent.view,t.addDataListener("brush_store",(function(e,t){var r=[[t[0].values[0][0],t[0].values[0][1]],[t[0].values[1][1],t[0].values[1][0]]],i=n.data.filter((function(e){var t=e[n.encoding.x],i=e[n.encoding.y],a=t>=r[0][0]&&t<=r[0][1]&&i>=r[1][0]&&i<=r[1][1];return a}));n.$emit("brush",i)})),this.view=t;case 5:case"end":return r.stop()}}),null,this)}},components:{Base:g}},b=m,w=(n("8168"),Object(h["a"])(b,o,s,!1,null,null,null)),x=w.exports,O={props:{points:{type:Array,required:!0}},data:function(){return{selection:[]}},methods:{onBrush:function(e){var t=u.a.differenceBy(e,this.selection,"id");t.length>0&&(this.selection=e)}},components:{Scatterplot:x}},S=O,_=(n("034f"),Object(h["a"])(S,i,a,!1,null,null,null)),j=_.exports,B=n("2f62");r["a"].use(B["a"]);var R=new B["a"].Store({state:{},mutations:{},actions:{},modules:{}});r["a"].config.productionTip=!1,new r["a"]({store:R,render:function(e){return e(j)}}).$mount("#app")},"6a75":function(e,t,n){"use strict";n("df14")},8168:function(e,t,n){"use strict";n("8634")},"85ec":function(e,t,n){},8634:function(e,t,n){},df14:function(e,t,n){}});
//# sourceMappingURL=app.4d00b0fd.js.map