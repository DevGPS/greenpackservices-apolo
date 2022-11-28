/*
 Highcharts JS v9.1.1 (2021-06-03)

 (c) 2009-2021 Torstein Honsi

 License: www.highcharts.com/license
*/
'use strict';(function(f){"object"===typeof module&&module.exports?(f["default"]=f,module.exports=f):"function"===typeof define&&define.amd?define("highcharts/modules/broken-axis",["highcharts"],function(l){f(l);f.Highcharts=l;return f}):f("undefined"!==typeof Highcharts?Highcharts:void 0)})(function(f){function l(f,q,l,h){f.hasOwnProperty(q)||(f[q]=h.apply(null,l))}f=f?f._modules:{};l(f,"Core/Axis/BrokenAxis.js",[f["Core/Axis/Axis.js"],f["Core/Series/Series.js"],f["Extensions/Stacking.js"],f["Core/Utilities.js"]],
function(f,l,z,h){var r=h.addEvent,q=h.find,x=h.fireEvent,A=h.isArray,m=h.isNumber,v=h.pick,w;(function(h){function w(){"undefined"!==typeof this.brokenAxis&&this.brokenAxis.setBreaks(this.options.breaks,!1)}function B(){this.brokenAxis&&this.brokenAxis.hasBreaks&&(this.options.ordinal=!1)}function C(){var b=this.brokenAxis;if(b&&b.hasBreaks){for(var c=this.tickPositions,g=this.tickPositions.info,e=[],a=0;a<c.length;a++)b.isInAnyBreak(c[a])||e.push(c[a]);this.tickPositions=e;this.tickPositions.info=
g}}function D(){this.brokenAxis||(this.brokenAxis=new y(this))}function E(){var b=this.options.connectNulls,c=this.points,g=this.xAxis,e=this.yAxis;if(this.isDirty)for(var a=c.length;a--;){var d=c[a],f=!(null===d.y&&!1===b)&&(g&&g.brokenAxis&&g.brokenAxis.isInAnyBreak(d.x,!0)||e&&e.brokenAxis&&e.brokenAxis.isInAnyBreak(d.y,!0));d.visible=f?!1:!1!==d.options.visible}}function F(){this.drawBreaks(this.xAxis,["x"]);this.drawBreaks(this.yAxis,v(this.pointArrayMap,["y"]))}function G(b,c){var g=this,e=
g.points,a,d,f,k;if(b&&b.brokenAxis&&b.brokenAxis.hasBreaks){var h=b.brokenAxis;c.forEach(function(c){a=h&&h.breakArray||[];d=b.isXAxis?b.min:v(g.options.threshold,b.min);e.forEach(function(e){k=v(e["stack"+c.toUpperCase()],e[c]);a.forEach(function(a){if(m(d)&&m(k)){f=!1;if(d<a.from&&k>a.to||d>a.from&&k<a.from)f="pointBreak";else if(d<a.from&&k>a.from&&k<a.to||d>a.from&&k>a.to&&k<a.from)f="pointInBreak";f&&x(b,f,{point:e,brk:a})}})})})}}function H(){var b=this.currentDataGrouping,c=b&&b.gapSize;b=
this.points.slice();var g=this.yAxis,e=this.options.gapSize,a=b.length-1,d;if(e&&0<a)for("value"!==this.options.gapUnit&&(e*=this.basePointRange),c&&c>e&&c>=this.basePointRange&&(e=c),d=void 0;a--;)d&&!1!==d.visible||(d=b[a+1]),c=b[a],!1!==d.visible&&!1!==c.visible&&(d.x-c.x>e&&(d=(c.x+d.x)/2,b.splice(a+1,0,{isNull:!0,x:d}),g.stacking&&this.options.stacking&&(d=g.stacking.stacks[this.stackKey][d]=new z(g,g.options.stackLabels,!1,d,this.stack),d.total=0)),d=c);return this.getGraphPath(b)}h.compose=
function(b,c){if(-1===b.keepProps.indexOf("brokenAxis")){b.keepProps.push("brokenAxis");var g=l.prototype;g.drawBreaks=G;g.gappedPath=H;r(b,"init",D);r(b,"afterInit",w);r(b,"afterSetTickPositions",C);r(b,"afterSetOptions",B);r(c,"afterGeneratePoints",E);r(c,"afterRender",F)}return b};var y=function(){function b(c){this.hasBreaks=!1;this.axis=c}b.isInBreak=function(c,b){var e=c.repeat||Infinity,a=c.from,d=c.to-c.from;b=b>=a?(b-a)%e:e-(a-b)%e;return c.inclusive?b<=d:b<d&&0!==b};b.lin2Val=function(c){var g=
this.brokenAxis;g=g&&g.breakArray;if(!g||!m(c))return c;var e;for(e=0;e<g.length;e++){var a=g[e];if(a.from>=c)break;else a.to<c?c+=a.len:b.isInBreak(a,c)&&(c+=a.len)}return c};b.val2Lin=function(c){var g=this.brokenAxis;g=g&&g.breakArray;if(!g||!m(c))return c;var e=c,a;for(a=0;a<g.length;a++){var d=g[a];if(d.to<=c)e-=d.len;else if(d.from>=c)break;else if(b.isInBreak(d,c)){e-=c-d.from;break}}return e};b.prototype.findBreakAt=function(c,b){return q(b,function(b){return b.from<c&&c<b.to})};b.prototype.isInAnyBreak=
function(c,g){var e=this.axis,a=e.options.breaks||[],d=a.length,f;if(d&&m(c)){for(;d--;)if(b.isInBreak(a[d],c)){var k=!0;f||(f=v(a[d].showPoints,!e.isXAxis))}var h=k&&g?k&&!f:k}return h};b.prototype.setBreaks=function(c,g){var e=this,a=e.axis,d=A(c)&&!!c.length;a.isDirty=e.hasBreaks!==d;e.hasBreaks=d;a.options.breaks=a.userOptions.breaks=c;a.forceRedraw=!0;a.series.forEach(function(a){a.isDirty=!0});d||a.val2lin!==b.val2Lin||(delete a.val2lin,delete a.lin2val);d&&(a.userOptions.ordinal=!1,a.lin2val=
b.lin2Val,a.val2lin=b.val2Lin,a.setExtremes=function(a,b,c,d,g){if(e.hasBreaks){for(var k=this.options.breaks||[],h;h=e.findBreakAt(a,k);)a=h.to;for(;h=e.findBreakAt(b,k);)b=h.from;b<a&&(b=a)}f.prototype.setExtremes.call(this,a,b,c,d,g)},a.setAxisTranslation=function(){f.prototype.setAxisTranslation.call(this);e.unitLength=void 0;if(e.hasBreaks){var c=a.options.breaks||[],d=[],g=[],h=v(a.pointRangePadding,0),l=0,t,n=a.userMin||a.min,u=a.userMax||a.max,q;c.forEach(function(a){t=a.repeat||Infinity;
m(n)&&m(u)&&(b.isInBreak(a,n)&&(n+=a.to%t-n%t),b.isInBreak(a,u)&&(u-=u%t-a.from%t))});c.forEach(function(a){p=a.from;t=a.repeat||Infinity;if(m(n)&&m(u)){for(;p-t>n;)p-=t;for(;p<n;)p+=t;for(q=p;q<u;q+=t)d.push({value:q,move:"in"}),d.push({value:q+a.to-a.from,move:"out",size:a.breakSize})}});d.sort(function(a,b){return a.value===b.value?("in"===a.move?0:1)-("in"===b.move?0:1):a.value-b.value});var r=0;var p=n;d.forEach(function(a){r+="in"===a.move?1:-1;1===r&&"in"===a.move&&(p=a.value);0===r&&m(p)&&
(g.push({from:p,to:a.value,len:a.value-p-(a.size||0)}),l+=a.value-p-(a.size||0))});e.breakArray=g;m(n)&&m(u)&&m(a.min)&&(e.unitLength=u-n-l+h,x(a,"afterBreaks"),a.staticScale?a.transA=a.staticScale:e.unitLength&&(a.transA*=(u-a.min+h)/e.unitLength),h&&(a.minPixelPadding=a.transA*(a.minPointOffset||0)),a.min=n,a.max=u)}});v(g,!0)&&a.chart.redraw()};return b}();h.Additions=y})(w||(w={}));return w});l(f,"masters/modules/broken-axis.src.js",[f["Core/Globals.js"],f["Core/Axis/BrokenAxis.js"]],function(f,
l){l.compose(f.Axis,f.Series)})});
//# sourceMappingURL=broken-axis.js.map