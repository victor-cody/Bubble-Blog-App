! function (e, t, o) {
	"use strict";
	var i = o(".select2"),
		n = "#blog-editor-container .editor",
		l = o("#blog-feature-image"),
		r = t.getElementById("blog-image-text"),
		a = o("#blogCustomFile");
	i.each((function () {
		var e = o(this);
		e.wrap('<div class="position-relative"></div>'), e.select2({
			dropdownAutoWidth: !0,
			width: "100%",
			dropdownParent: e.parent()
		})
	}));
	var s = Quill.import("formats/font");
	s.whitelist = ["sofia", "slabo", "roboto", "inconsolata", "ubuntu"], Quill.register(s, !0);
	new Quill(n, {
		bounds: n,
		modules: {
			formula: !0,
			syntax: !0,
			toolbar: [
				[{
					font: []
				}, {
					size: []
				}],
				["bold", "italic", "underline", "strike"],
				[{
					color: []
				}, {
					background: []
				}],
				[{
					script: "super"
				}, {
					script: "sub"
				}],
				[{
					header: "1"
				}, {
					header: "2"
				}, "blockquote", "code-block"],
				[{
					list: "ordered"
				}, {
					list: "bullet"
				}, {
					indent: "-1"
				}, {
					indent: "+1"
				}],
				["direction", {
					align: []
				}],
				["link", "image", "video", "formula"],
				["clean"]
			]
		},
		theme: "snow"
	});
	a.length && o(a).on("change", (function (e) {
		var t = new FileReader,
			o = e.target.files;
		t.onload = function () {
			l.length && l.attr("src", t.result)
		}, t.readAsDataURL(o[0]), r.innerHTML = a.val()
	}))
}(window, document, jQuery);
