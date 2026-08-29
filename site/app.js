"use strict";

(function () {
  var HASH = "4e225ca4509cd07305ae9336ff17706ea4f9af7cb6cfd8a17690bc0528fa61be";
  var GATE_KEY = "elteknik-gate";

  var WEEKS = [
    {
      title: "Vecka 1 m1",
      items: [
        {"label": "Lektion 1.1 Stötar", "path": "kurs/lektioner/1.1-stotar.md"},
        {"label": "Kapitel 1 Elsäkerhet", "path": "bok/kapitel-01-elsakerhet-stotar.md", "figure": "bok/figur-1-1-stotvag-ventil.png", "caption": "Figur 1.1"},
        {"label": "Classroom vecka 1", "path": "kurs/lararhandledning/classroom-v1-vecka1.md"},
        {"label": "Quiz vecka 1", "path": "kurs/lararhandledning/classroom-v1-quiz.md"},
        {"label": "Bildspel vecka 1", "path": "kurs/lararhandledning/classroom-v1-slides.md"}
      ]
    },
    {
      title: "Vecka 2",
      items: [
        {"label": "Lektion 2.1 Isolering", "path": "kurs/lektioner/2.1-isolering.md"},
        {"label": "Kapitel 2 Isolering", "path": "bok/kapitel-02-isolering-fore-arbete.md", "figure": "bok/figur-2-1-isolering-kedja.png", "caption": "Figur 2.1"},
        {"label": "Classroom vecka 2", "path": "kurs/lararhandledning/classroom-v2-vecka2.md"},
        {"label": "Quiz vecka 2", "path": "kurs/lararhandledning/classroom-v2-quiz.md"},
        {"label": "Bildspel vecka 2", "path": "kurs/lararhandledning/classroom-v2-slides.md"}
      ]
    },
    {
      title: "Vecka 3",
      items: [
        {"label": "Lektion 3.1 DC", "path": "kurs/lektioner/3.1-dc.md"},
        {"label": "Kapitel 3 Resistiv DC", "path": "bok/kapitel-03-resistiv-dc.md", "figure": "bok/figur-3-1-dc-matning.png", "caption": "Figur 3.1"},
        {"label": "Classroom vecka 3", "path": "kurs/lararhandledning/classroom-v3-vecka3.md"},
        {"label": "Quiz vecka 3", "path": "kurs/lararhandledning/classroom-v3-quiz.md"},
        {"label": "Bildspel vecka 3", "path": "kurs/lararhandledning/classroom-v3-slides.md"}
      ]
    },
    {
      title: "Vecka 4",
      items: [
        {"label": "Lektion 4.1 Enfas AC", "path": "kurs/lektioner/4.1-enfas-ac.md"},
        {"label": "Kapitel 4 Enfas AC", "path": "bok/kapitel-04-enfas-ac.md", "figure": "bok/figur-4-1-enfas-ac.png", "caption": "Figur 4.1"},
        {"label": "Classroom vecka 4", "path": "kurs/lararhandledning/classroom-v4-vecka4.md"},
        {"label": "Quiz vecka 4", "path": "kurs/lararhandledning/classroom-v4-quiz.md"},
        {"label": "Bildspel vecka 4", "path": "kurs/lararhandledning/classroom-v4-slides.md"}
      ]
    },
    {
      title: "Vecka 5",
      items: [
        {"label": "Lektion 5.1 Trefas", "path": "kurs/lektioner/5.1-trefas.md"},
        {"label": "Kapitel 5 Trefas", "path": "bok/kapitel-05-trefas-spanningstyper.md", "figure": "bok/figur-5-1-trefas-spanning.png", "caption": "Figur 5.1"},
        {"label": "Classroom vecka 5", "path": "kurs/lararhandledning/classroom-v5-vecka5.md"},
        {"label": "Quiz vecka 5", "path": "kurs/lararhandledning/classroom-v5-quiz.md"},
        {"label": "Bildspel vecka 5", "path": "kurs/lararhandledning/classroom-v5-slides.md"}
      ]
    },
    {
      title: "Vecka 6",
      items: [
        {"label": "Lektion 6.1 Maskiner", "path": "kurs/lektioner/6.1-maskiner.md"},
        {"label": "Kapitel 6 Maskiner", "path": "bok/kapitel-06-maskiner.md", "figure": "bok/figur-6-1-maskiner.png", "caption": "Figur 6.1"},
        {"label": "Classroom vecka 6", "path": "kurs/lararhandledning/classroom-v6-vecka6.md"},
        {"label": "Quiz vecka 6", "path": "kurs/lararhandledning/classroom-v6-quiz.md"},
        {"label": "Bildspel vecka 6", "path": "kurs/lararhandledning/classroom-v6-slides.md"}
      ]
    },
    {
      title: "Vecka 7",
      items: [
        {"label": "Lektion 7.1 Eltavla", "path": "kurs/lektioner/7.1-eltavla.md"},
        {"label": "Kapitel 7 Eltavla", "path": "bok/kapitel-07-eltavla.md", "figure": "bok/figur-7-1-eltavla.png", "caption": "Figur 7.1"},
        {"label": "Classroom vecka 7", "path": "kurs/lararhandledning/classroom-v7-vecka7.md"},
        {"label": "Quiz vecka 7", "path": "kurs/lararhandledning/classroom-v7-quiz.md"},
        {"label": "Bildspel vecka 7", "path": "kurs/lararhandledning/classroom-v7-slides.md"}
      ]
    },
    {
      title: "Vecka 7b m8",
      items: [
        {"label": "Lektion 8.1 Verktyg", "path": "kurs/lektioner/8.1-verktyg.md"},
        {"label": "Kapitel 8 Verktyg", "path": "bok/kapitel-08-verktyg.md", "figure": "bok/figur-8-1-verktyg.png", "caption": "Figur 8.1"},
        {"label": "Classroom vecka 7b", "path": "kurs/lararhandledning/classroom-v7b-vecka7.md"},
        {"label": "Quiz m8", "path": "kurs/lararhandledning/classroom-v8-quiz.md"},
        {"label": "Bildspel m8", "path": "kurs/lararhandledning/classroom-v8-slides.md"}
      ]
    },
    {
      title: "Vecka 8 m9",
      items: [
        {"label": "Lektion 9.1 Ritningar", "path": "kurs/lektioner/9.1-ritningar.md"},
        {"label": "Kapitel 9 Ritningar", "path": "bok/kapitel-09-ritningar.md", "figure": "bok/figur-9-1-ritningar.png", "caption": "Figur 9.1"},
        {"label": "Classroom vecka 8", "path": "kurs/lararhandledning/classroom-v8-vecka8.md"},
        {"label": "Quiz m9", "path": "kurs/lararhandledning/classroom-v9-quiz.md"},
        {"label": "Bildspel m9", "path": "kurs/lararhandledning/classroom-v9-slides.md"}
      ]
    },
    {
      title: "Vecka 8b m10",
      items: [
        {"label": "Lektion 10.1 Hållkrets", "path": "kurs/lektioner/10.1-hallkrets.md"},
        {"label": "Kapitel 10 Hållkrets", "path": "bok/kapitel-10-hallkrets.md", "figure": "bok/figur-10-1-hallkrets.png", "caption": "Figur 10.1"},
        {"label": "Classroom vecka 8b", "path": "kurs/lararhandledning/classroom-v8b-vecka8.md"},
        {"label": "Quiz m10", "path": "kurs/lararhandledning/classroom-v10-quiz.md"},
        {"label": "Bildspel m10", "path": "kurs/lararhandledning/classroom-v10-slides.md"}
      ]
    },
    {
      title: "Vecka 9 m11",
      items: [
        {"label": "Lektion 11.1 Arbete IP intyg", "path": "kurs/lektioner/11.1-arbete-ip-intyg.md"},
        {"label": "Kapitel 11 Elarbete IP intyg", "path": "bok/kapitel-11-elarbete-ip-intyg.md", "figure": "bok/figur-11-1-arbete-ip-intyg.png", "caption": "Figur 11.1"},
        {"label": "Classroom vecka 9", "path": "kurs/lararhandledning/classroom-v9-vecka9.md"},
        {"label": "Quiz m11", "path": "kurs/lararhandledning/classroom-v11-quiz.md"},
        {"label": "Bildspel m11", "path": "kurs/lararhandledning/classroom-v11-slides.md"}
      ]
    },
    {
      title: "Vecka 9b m12",
      items: [
        {"label": "Lektion 12.1 Felsökning", "path": "kurs/lektioner/12.1-felsokning.md"},
        {"label": "Kapitel 12 Felsökning", "path": "bok/kapitel-12-felsokning.md", "figure": "bok/figur-12-1-felsokning.png", "caption": "Figur 12.1"},
        {"label": "Classroom vecka 9b", "path": "kurs/lararhandledning/classroom-v9b-vecka9.md"},
        {"label": "Quiz m12", "path": "kurs/lararhandledning/classroom-v12-quiz.md"},
        {"label": "Bildspel m12", "path": "kurs/lararhandledning/classroom-v12-slides.md"}
      ]
    }
  ];
  var EXTRA = [
    {"label": "Kurskarta", "path": "kurs/kurskarta/kurskarta-v2.md"},
    {"label": "Labbdag", "path": "kurs/labbdag-v2.md"},
    {"label": "Skriftligt prov (elev)", "path": "kurs/prov/skriftligt-prov-elev.md"},
    {"label": "Classroom prov", "path": "kurs/lararhandledning/classroom-v-prov-vecka9.md"}
  ];

  function byId(id) { return document.getElementById(id); }
  function toHex(buf) {
    return Array.from(new Uint8Array(buf)).map(function (b) {
      return b.toString(16).padStart(2, "0");
    }).join("");
  }
  function sha256hex(str) {
    return crypto.subtle.digest("SHA-256", new TextEncoder().encode(str)).then(toHex);
  }
  function isOpen() { return sessionStorage.getItem(GATE_KEY) === "1"; }
  function setOpen(v) {
    if (v) sessionStorage.setItem(GATE_KEY, "1");
    else sessionStorage.removeItem(GATE_KEY);
  }
  function hasFacit(path) { return /facit/i.test(path || ""); }
  function okPath(path) {
    if (!path || hasFacit(path)) return false;
    if (path.indexOf("..") !== -1) return false;
    if (!/\.md$/i.test(path)) return false;
    return path.indexOf("kurs/") === 0 || path.indexOf("bok/") === 0;
  }
  function hashPath() {
    return decodeURIComponent((location.hash || "").replace(/^#\/?/, "")).trim();
  }
  function resolveRel(baseDir, rel) {
    var parts = (baseDir + "/" + rel).split("/");
    var out = [];
    for (var i = 0; i < parts.length; i++) {
      var p = parts[i];
      if (!p || p === ".") continue;
      if (p === "..") out.pop();
      else out.push(p);
    }
    return out.join("/");
  }
  function rewriteMd(md, mdPath) {
    var dir = mdPath.replace(/\/[^/]+$/, "");
    return md.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, function (m, alt, src) {
      src = String(src).trim();
      if (/^(https?:|data:|\/)/i.test(src)) return m;
      return "![" + alt + "](" + resolveRel(dir, src) + ")";
    });
  }
  function findItem(path) {
    var i, j;
    for (i = 0; i < WEEKS.length; i++) {
      for (j = 0; j < WEEKS[i].items.length; j++) {
        if (WEEKS[i].items[j].path === path) return WEEKS[i].items[j];
      }
    }
    for (i = 0; i < EXTRA.length; i++) {
      if (EXTRA[i].path === path) return EXTRA[i];
    }
    return null;
  }
  function renderNav() {
    var nav = byId("nav");
    var path = hashPath();
    var html = "";
    html += "<a href=\"#/\"" + (!path ? " class=\"active\"" : "") + ">Start</a>";
    for (var i = 0; i < WEEKS.length; i++) {
      var w = WEEKS[i];
      html += "<details open><summary>" + w.title + "</summary><div class=\"week-links\">";
      for (var j = 0; j < w.items.length; j++) {
        var it = w.items[j];
        var cls = it.path === path ? " class=\"active\"" : "";
        html += "<a href=\"#/" + it.path + "\"" + cls + ">" + it.label + "</a>";
      }
      html += "</div></details>";
    }
    html += "<h2>Extra</h2>";
    for (var k = 0; k < EXTRA.length; k++) {
      var ex = EXTRA[k];
      var cls2 = ex.path === path ? " class=\"active\"" : "";
      html += "<a href=\"#/" + ex.path + "\"" + cls2 + ">" + ex.label + "</a>";
    }
    nav.innerHTML = html;
  }
  function homeHtml() {
    return [
      "<div class=\"home\">",
      "<p class=\"kicker\">YH-kurs \u00b7 45 po\u00e4ng</p>",
      "<h2>Elteknik och ell\u00e4ra</h2>",
      "<p>Nio veckor. Tolv moduler. Distans f\u00f6rst, en fysisk labbdag efter vecka 8.</p>",
      "<ol>",
      "<li><strong>Vecka 1</strong> \u2014 Els\u00e4kerhet och st\u00f6tar (m1)</li>",
      "<li><strong>Vecka 2</strong> \u2014 Isolering f\u00f6re arbete (m2)</li>",
      "<li><strong>Vecka 3</strong> \u2014 Resistiv DC (m3)</li>",
      "<li><strong>Vecka 4</strong> \u2014 Enfas AC (m4)</li>",
      "<li><strong>Vecka 5</strong> \u2014 Trefas (m5)</li>",
      "<li><strong>Vecka 6</strong> \u2014 Maskiner (m6)</li>",
      "<li><strong>Vecka 7</strong> \u2014 Eltavla (m7) och verktyg (m8)</li>",
      "<li><strong>Vecka 8</strong> \u2014 Ritningar (m9) och h\u00e5llkrets (m10)</li>",
      "<li><strong>Vecka 9</strong> \u2014 Elarbete, IP, intyg (m11), fels\u00f6kning (m12) och skriftligt prov</li>",
      "</ol>",
      "<p class=\"warn\">L\u00e4rarfacit till det skriftliga provet ligger inte p\u00e5 den h\u00e4r sajten.</p>",
      "</div>"
    ].join("");
  }
  function showHome() {
    byId("main").innerHTML = homeHtml();
    renderNav();
  }
  function showBlocked() {
    byId("main").innerHTML = "<p class=\"page-err\">Den sidan finns inte p\u00e5 studentsajten.</p>";
    renderNav();
  }
  function loadPage(path) {
    if (!path || path === "/") { showHome(); return; }
    if (hasFacit(path) || !okPath(path)) { showBlocked(); return; }
    var item = findItem(path);
    fetch(path).then(function (res) {
      if (!res.ok) throw new Error(String(res.status));
      return res.text();
    }).then(function (md) {
      var html = "";
      if (item && item.figure) {
        html += "<figure class=\"figure\"><img src=\"" + item.figure + "\" alt=\"" + (item.caption || "") + "\">";
        if (item.caption) html += "<figcaption>" + item.caption + "</figcaption>";
        html += "</figure>";
      }
      html += marked.parse(rewriteMd(md, path));
      byId("main").innerHTML = html;
      renderNav();
      window.scrollTo(0, 0);
    }).catch(function () {
      byId("main").innerHTML = "<p class=\"page-err\">Kunde inte l\u00e4sa sidan.</p>";
      renderNav();
    });
  }
  function showApp() {
    byId("gate").hidden = true;
    byId("app").hidden = false;
    loadPage(hashPath());
  }
  function showGate() {
    byId("gate").hidden = false;
    byId("app").hidden = true;
  }
  function onHash() {
    if (!isOpen()) { showGate(); return; }
    loadPage(hashPath());
  }
  function initGate() {
    var form = byId("gate-form");
    var err = byId("gate-err");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var pw = byId("pw").value.trim();
      sha256hex(pw).then(function (h) {
        if (h === HASH) {
          err.hidden = true;
          setOpen(true);
          showApp();
        } else {
          err.hidden = false;
        }
      });
    });
    byId("lock-btn").addEventListener("click", function () {
      setOpen(false);
      byId("pw").value = "";
      showGate();
    });
    window.addEventListener("hashchange", onHash);
    if (isOpen()) showApp();
    else showGate();
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initGate);
  } else {
    initGate();
  }
})();
