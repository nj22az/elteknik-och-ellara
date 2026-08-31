"use strict";

(function () {
  var ROLES = {
    student: { hash: "4e225ca4509cd07305ae9336ff17706ea4f9af7cb6cfd8a17690bc0528fa61be", label: "Elev" },
    teacher: { hash: "0b19ce7a70145305c3b32e03fcf6de104e6c9ced29337ec17f73cca67720f235", label: "Lärare" },
    book: { hash: "d307be2aec862a45fb7b29dac54f1753829a6972aa5b9a0df6b9f6a021110a89", label: "Bok" }
  };
  var GATE_KEY = "elteknik-gate";
  var ROLE_KEY = "elteknik-role";

  var WEEKS = [
    {
      title: "V1 · M01",
      items: [
        {"label": "Lektion 1.1 Stötar", "path": "kurs/lektioner/1.1-stotar.md"},
        {"label": "Kapitel 1 Elsäkerhet", "path": "bok/kapitel-01-elsakerhet-stotar.md", "figure": "bok/figur-1-1-stotvag-ventil.png", "caption": "Figur 1.1"},
        {"label": "Classroom vecka 1", "path": "kurs/lararhandledning/classroom-v1-vecka1.md"},
        {"label": "Quiz vecka 1", "path": "kurs/lararhandledning/classroom-v1-quiz.md"},
        {"label": "Bildspel vecka 1", "path": "kurs/lararhandledning/classroom-v1-slides.md"}
      ]
    },
    {
      title: "V2 · M02",
      items: [
        {"label": "Lektion 2.1 Isolering", "path": "kurs/lektioner/2.1-isolering.md"},
        {"label": "Kapitel 2 Isolering", "path": "bok/kapitel-02-isolering-fore-arbete.md", "figure": "bok/figur-2-1-isolering-kedja.png", "caption": "Figur 2.1"},
        {"label": "Classroom vecka 2", "path": "kurs/lararhandledning/classroom-v2-vecka2.md"},
        {"label": "Quiz vecka 2", "path": "kurs/lararhandledning/classroom-v2-quiz.md"},
        {"label": "Bildspel vecka 2", "path": "kurs/lararhandledning/classroom-v2-slides.md"}
      ]
    },
    {
      title: "V3 · M03",
      items: [
        {"label": "Lektion 3.1 DC", "path": "kurs/lektioner/3.1-dc.md"},
        {"label": "Kapitel 3 Resistiv DC", "path": "bok/kapitel-03-resistiv-dc.md", "figure": "bok/figur-3-1-dc-matning.png", "caption": "Figur 3.1"},
        {"label": "Classroom vecka 3", "path": "kurs/lararhandledning/classroom-v3-vecka3.md"},
        {"label": "Quiz vecka 3", "path": "kurs/lararhandledning/classroom-v3-quiz.md"},
        {"label": "Bildspel vecka 3", "path": "kurs/lararhandledning/classroom-v3-slides.md"}
      ]
    },
    {
      title: "V4 · M04",
      items: [
        {"label": "Lektion 4.1 Enfas AC", "path": "kurs/lektioner/4.1-enfas-ac.md"},
        {"label": "Kapitel 4 Enfas AC", "path": "bok/kapitel-04-enfas-ac.md", "figure": "bok/figur-4-1-enfas-ac.png", "caption": "Figur 4.1"},
        {"label": "Classroom vecka 4", "path": "kurs/lararhandledning/classroom-v4-vecka4.md"},
        {"label": "Quiz vecka 4", "path": "kurs/lararhandledning/classroom-v4-quiz.md"},
        {"label": "Bildspel vecka 4", "path": "kurs/lararhandledning/classroom-v4-slides.md"}
      ]
    },
    {
      title: "V5 · M05",
      items: [
        {"label": "Lektion 5.1 Trefas", "path": "kurs/lektioner/5.1-trefas.md"},
        {"label": "Kapitel 5 Trefas", "path": "bok/kapitel-05-trefas-spanningstyper.md", "figure": "bok/figur-5-1-trefas-spanning.png", "caption": "Figur 5.1"},
        {"label": "Classroom vecka 5", "path": "kurs/lararhandledning/classroom-v5-vecka5.md"},
        {"label": "Quiz vecka 5", "path": "kurs/lararhandledning/classroom-v5-quiz.md"},
        {"label": "Bildspel vecka 5", "path": "kurs/lararhandledning/classroom-v5-slides.md"}
      ]
    },
    {
      title: "V6 · M06",
      items: [
        {"label": "Lektion 6.1 Maskiner", "path": "kurs/lektioner/6.1-maskiner.md"},
        {"label": "Kapitel 6 Maskiner", "path": "bok/kapitel-06-maskiner.md", "figure": "bok/figur-6-1-maskiner.png", "caption": "Figur 6.1"},
        {"label": "Classroom vecka 6", "path": "kurs/lararhandledning/classroom-v6-vecka6.md"},
        {"label": "Quiz vecka 6", "path": "kurs/lararhandledning/classroom-v6-quiz.md"},
        {"label": "Bildspel vecka 6", "path": "kurs/lararhandledning/classroom-v6-slides.md"}
      ]
    },
    {
      title: "V7 · M07",
      items: [
        {"label": "Lektion 7.1 Eltavla", "path": "kurs/lektioner/7.1-eltavla.md"},
        {"label": "Kapitel 7 Eltavla", "path": "bok/kapitel-07-eltavla.md", "figure": "bok/figur-7-1-eltavla.png", "caption": "Figur 7.1"},
        {"label": "Classroom vecka 7", "path": "kurs/lararhandledning/classroom-v7-vecka7.md"},
        {"label": "Quiz vecka 7", "path": "kurs/lararhandledning/classroom-v7-quiz.md"},
        {"label": "Bildspel vecka 7", "path": "kurs/lararhandledning/classroom-v7-slides.md"}
      ]
    },
    {
      title: "V7 · M08",
      items: [
        {"label": "Lektion 8.1 Verktyg", "path": "kurs/lektioner/8.1-verktyg.md"},
        {"label": "Kapitel 8 Verktyg", "path": "bok/kapitel-08-verktyg.md", "figure": "bok/figur-8-1-verktyg.png", "caption": "Figur 8.1"},
        {"label": "Classroom vecka 7b", "path": "kurs/lararhandledning/classroom-v7b-vecka7.md"},
        {"label": "Quiz M08", "path": "kurs/lararhandledning/classroom-v8-quiz.md"},
        {"label": "Bildspel M08", "path": "kurs/lararhandledning/classroom-v8-slides.md"}
      ]
    },
    {
      title: "V8 · M09",
      items: [
        {"label": "Lektion 9.1 Ritningar", "path": "kurs/lektioner/9.1-ritningar.md"},
        {"label": "Kapitel 9 Ritningar", "path": "bok/kapitel-09-ritningar.md", "figure": "bok/figur-9-1-ritningar.png", "caption": "Figur 9.1"},
        {"label": "Classroom vecka 8", "path": "kurs/lararhandledning/classroom-v8-vecka8.md"},
        {"label": "Quiz M09", "path": "kurs/lararhandledning/classroom-v9-quiz.md"},
        {"label": "Bildspel M09", "path": "kurs/lararhandledning/classroom-v9-slides.md"}
      ]
    },
    {
      title: "V8 · M10",
      items: [
        {"label": "Lektion 10.1 Hållkrets", "path": "kurs/lektioner/10.1-hallkrets.md"},
        {"label": "Kapitel 10 Hållkrets", "path": "bok/kapitel-10-hallkrets.md", "figure": "bok/figur-10-1-hallkrets.png", "caption": "Figur 10.1"},
        {"label": "Classroom vecka 8b", "path": "kurs/lararhandledning/classroom-v8b-vecka8.md"},
        {"label": "Quiz M10", "path": "kurs/lararhandledning/classroom-v10-quiz.md"},
        {"label": "Bildspel M10", "path": "kurs/lararhandledning/classroom-v10-slides.md"}
      ]
    },
    {
      title: "V9 · M11",
      items: [
        {"label": "Lektion 11.1 Arbete IP intyg", "path": "kurs/lektioner/11.1-arbete-ip-intyg.md"},
        {"label": "Kapitel 11 Elarbete IP intyg", "path": "bok/kapitel-11-elarbete-ip-intyg.md", "figure": "bok/figur-11-1-arbete-ip-intyg.png", "caption": "Figur 11.1"},
        {"label": "Classroom vecka 9", "path": "kurs/lararhandledning/classroom-v9-vecka9.md"},
        {"label": "Quiz M11", "path": "kurs/lararhandledning/classroom-v11-quiz.md"},
        {"label": "Bildspel M11", "path": "kurs/lararhandledning/classroom-v11-slides.md"}
      ]
    },
    {
      title: "V9 · M12",
      items: [
        {"label": "Lektion 12.1 Felsökning", "path": "kurs/lektioner/12.1-felsokning.md"},
        {"label": "Kapitel 12 Felsökning", "path": "bok/kapitel-12-felsokning.md", "figure": "bok/figur-12-1-felsokning.png", "caption": "Figur 12.1"},
        {"label": "Classroom vecka 9b", "path": "kurs/lararhandledning/classroom-v9b-vecka9.md"},
        {"label": "Quiz M12", "path": "kurs/lararhandledning/classroom-v12-quiz.md"},
        {"label": "Bildspel M12", "path": "kurs/lararhandledning/classroom-v12-slides.md"}
      ]
    }
  ];
  var EXTRA = [
    {"label": "Kurskarta", "path": "kurs/kurskarta/kurskarta-v2.md"},
    {"label": "Labbdag", "path": "kurs/labbdag-v2.md"},
    {"label": "Skriftligt prov (elev)", "path": "kurs/prov/skriftligt-prov-elev.md"},
    {"label": "Classroom prov", "path": "kurs/lararhandledning/classroom-v-prov-vecka9.md"}
  ];


  var EXTRA_FACIT = {"label": "Skriftligt prov (facit)", "path": "kurs/prov/skriftligt-prov-facit.md"};
  var PROGRESS_KEY = "elteknik-progress";
  var STEP_NAME = { lektion: "Lektion", bok: "Kapitel", slides: "Bildspel", quiz: "Quiz", classroom: "Lärarhandledning" };
  var STUDENT_STEPS = ["lektion", "bok", "slides", "quiz"];
  var MODULES = [
    { hub: "1", cal: "1", m: "M01", name: "Elsäkerhet och stötar", chap: "Elsäkerhet, stötar" },
    { hub: "2", cal: "2", m: "M02", name: "Isolering före arbete", chap: "Isolering före arbete" },
    { hub: "3", cal: "3", m: "M03", name: "Resistiv DC", chap: "Resistiv DC" },
    { hub: "4", cal: "4", m: "M04", name: "Enfas AC", chap: "Enfas AC" },
    { hub: "5", cal: "5", m: "M05", name: "Trefas", chap: "Trefas, spänningstyper" },
    { hub: "6", cal: "6", m: "M06", name: "Maskiner", chap: "Maskiner" },
    { hub: "7", cal: "7", m: "M07", name: "Eltavla", chap: "Eltavla" },
    { hub: "7b", cal: "7", m: "M08", name: "Verktyg", chap: "Verktyg" },
    { hub: "8", cal: "8", m: "M09", name: "Ritningar", chap: "Ritningar" },
    { hub: "8b", cal: "8", m: "M10", name: "Hållkrets", chap: "Hållkrets" },
    { hub: "9", cal: "9", m: "M11", name: "Elarbete, IP, intyg", chap: "Elarbete, IP, intyg" },
    { hub: "9b", cal: "9", m: "M12", name: "Felsökning", chap: "Felsökning" }
  ];
  var CAL_IDS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"];
  var HUB_IDS = ["1", "2", "3", "4", "5", "6", "7", "7b", "8", "8b", "9", "9b"];
  var PACKS = {
    "1": {
      elevFiles: [
        { label: "Elevblad stötväg (PDF)", href: "kurs/classroom-pack/vecka-01/elev-stotvag.pdf" },
        { label: "Elevblad stötväg (Word)", href: "kurs/classroom-pack/vecka-01/elev-stotvag.docx" },
        { label: "Lektion 1.1 Stötar (PDF)", href: "kurs/classroom-pack/vecka-01/lektion-1.1-stotar.pdf" },
        { label: "Lektion 1.1 Stötar (Word)", href: "kurs/classroom-pack/vecka-01/lektion-1.1-stotar.docx" }
      ],
      uppgiftFiles: [
        { label: "Elevblad stötväg (PDF)", href: "kurs/classroom-pack/vecka-01/elev-stotvag.pdf" },
        { label: "Elevblad stötväg (Word)", href: "kurs/classroom-pack/vecka-01/elev-stotvag.docx" }
      ],
      materialFiles: [
        { label: "Lektion 1.1 Stötar (PDF)", href: "kurs/classroom-pack/vecka-01/lektion-1.1-stotar.pdf" },
        { label: "Lektion 1.1 Stötar (Word)", href: "kurs/classroom-pack/vecka-01/lektion-1.1-stotar.docx" }
      ],
      elevMd: "kurs/elevblad/v1-stotvag-elev.md",
      larareFiles: [
        { label: "Facit stötväg (PDF)", href: "kurs/classroom-pack/vecka-01/larare-stotvag-facit.pdf" },
        { label: "Facit stötväg (Word)", href: "kurs/classroom-pack/vecka-01/larare-stotvag-facit.docx" },
        { label: "Inlägg vecka 1 (PDF)", href: "kurs/classroom-pack/vecka-01/larare-inlagg-vecka1.pdf" },
        { label: "Inlägg vecka 1 (Word)", href: "kurs/classroom-pack/vecka-01/larare-inlagg-vecka1.docx" }
      ],
      pptx: "pptx/vecka-01.pptx",
      quizzes: ["kurs/lararhandledning/classroom-v1-quiz.md"],
      inlagg: "kurs/lararhandledning/classroom-v1-vecka1.md"
    },
    "2": {
      elevFiles: [
        { label: "Elevblad meggerkort (PDF)", href: "kurs/classroom-pack/vecka-02/elev-meggerkort.pdf" },
        { label: "Elevblad meggerkort (Word)", href: "kurs/classroom-pack/vecka-02/elev-meggerkort.docx" },
        { label: "Lektion 2.1 Isolering (PDF)", href: "kurs/classroom-pack/vecka-02/lektion-2.1-isolering.pdf" },
        { label: "Lektion 2.1 Isolering (Word)", href: "kurs/classroom-pack/vecka-02/lektion-2.1-isolering.docx" }
      ],
      uppgiftFiles: [
        { label: "Elevblad meggerkort (PDF)", href: "kurs/classroom-pack/vecka-02/elev-meggerkort.pdf" },
        { label: "Elevblad meggerkort (Word)", href: "kurs/classroom-pack/vecka-02/elev-meggerkort.docx" }
      ],
      materialFiles: [
        { label: "Lektion 2.1 Isolering (PDF)", href: "kurs/classroom-pack/vecka-02/lektion-2.1-isolering.pdf" },
        { label: "Lektion 2.1 Isolering (Word)", href: "kurs/classroom-pack/vecka-02/lektion-2.1-isolering.docx" }
      ],
      elevMd: "kurs/elevblad/v2-meggerkort-elev.md",
      larareFiles: [
        { label: "Facit meggerkort (PDF)", href: "kurs/classroom-pack/vecka-02/larare-meggerkort-facit.pdf" },
        { label: "Facit meggerkort (Word)", href: "kurs/classroom-pack/vecka-02/larare-meggerkort-facit.docx" },
        { label: "Inlägg vecka 2 (PDF)", href: "kurs/classroom-pack/vecka-02/larare-inlagg-vecka2.pdf" },
        { label: "Inlägg vecka 2 (Word)", href: "kurs/classroom-pack/vecka-02/larare-inlagg-vecka2.docx" }
      ],
      pptx: "pptx/vecka-02.pptx",
      quizzes: ["kurs/lararhandledning/classroom-v2-quiz.md"],
      inlagg: "kurs/lararhandledning/classroom-v2-vecka2.md"
    }
  };
  function byId(id) { return document.getElementById(id); }
  function toHex(buf) {
    return Array.from(new Uint8Array(buf)).map(function (b) {
      return b.toString(16).padStart(2, "0");
    }).join("");
  }
  function sha256hex(str) {
    return crypto.subtle.digest("SHA-256", new TextEncoder().encode(str)).then(toHex);
  }
  function getRole() { return sessionStorage.getItem(ROLE_KEY) || ""; }
  function isOpen() { return sessionStorage.getItem(GATE_KEY) === "1" && !!ROLES[getRole()]; }
  function setSession(role) {
    sessionStorage.setItem(GATE_KEY, "1");
    sessionStorage.setItem(ROLE_KEY, role);
  }
  function clearSession() {
    sessionStorage.removeItem(GATE_KEY);
    sessionStorage.removeItem(ROLE_KEY);
  }
  function isTeacher() { return getRole() === "teacher"; }
  function isStudent() { return getRole() === "student"; }
  function isBook() { return getRole() === "book"; }
  function extraList() {
    if (isTeacher()) return EXTRA.concat([EXTRA_FACIT]);
    if (isStudent()) {
      return EXTRA.filter(function (x) {
        return x.path.indexOf("classroom") === -1 && !hasFacit(x.path);
      });
    }
    return [];
  }
  function hasFacit(path) { return /facit/i.test(path || ""); }
  function isStudentForbidden(path) {
    var s = String(path || "");
    if (hasFacit(s)) return true;
    if (/larare-/i.test(s)) return true;
    if (/\.pptx/i.test(s)) return true;
    return false;
  }
  function studentHrefOk(href) {
    var s = String(href || "");
    if (!s || s.indexOf("..") !== -1) return false;
    if (isStudentForbidden(s)) return false;
    var base = s.split("?")[0].split("#")[0].split("/").pop();
    if (/^elev-/i.test(base) && /\.(pdf|docx)$/i.test(base)) return true;
    if (/^lektion-/i.test(base) && /\.(pdf|docx)$/i.test(base)) return true;
    return false;
  }
  function calPad(cal) {
    cal = String(cal || "").replace(/b$/, "");
    return cal.length < 2 ? "0" + cal : cal;
  }
  function weekPack(cal) {
    cal = String(cal || "").replace(/b$/, "");
    var known = PACKS[cal];
    var quizzes = [];
    var hubs = calHubs(cal);
    var i, idx, items, j;
    for (i = 0; i < hubs.length; i++) {
      idx = hubIndex(hubs[i]);
      if (idx < 0) continue;
      items = WEEKS[idx].items;
      for (j = 0; j < items.length; j++) {
        if (classify(items[j]) === "quiz") quizzes.push(items[j].path);
      }
    }
    if (known) {
      return {
        ready: true,
        cal: cal,
        elevFiles: known.elevFiles,
        uppgiftFiles: known.uppgiftFiles,
        materialFiles: known.materialFiles || [],
        elevMd: known.elevMd || "",
        larareFiles: known.larareFiles,
        pptx: known.pptx,
        quizzes: known.quizzes.slice(),
        inlagg: known.inlagg
      };
    }
    return {
      ready: false,
      cal: cal,
      elevFiles: [],
      uppgiftFiles: [],
      materialFiles: [],
      elevMd: "",
      larareFiles: [],
      pptx: "pptx/vecka-" + calPad(cal) + ".pptx",
      quizzes: quizzes,
      inlagg: ""
    };
  }
  function weekHeroHtml(cal) {
    var mods = calModules(cal);
    var html = "<div class=\"week-hero\">" + stationHtml("V" + cal, "week-num active");
    html += "<span class=\"lozenge-row\">";
    for (var i = 0; i < mods.length; i++) html += lozengeHtml(mods[i].m);
    if (mods.length > 1) html += "<span class=\"xfer\">byte</span>";
    html += "</span>";
    html += "<div><h2>Vecka " + cal + "</h2></div></div>";
    return html;
  }
  function packDl(href, label) {
    return "<a class=\"pack-download\" href=\"" + href + "\" download target=\"_blank\" rel=\"noopener\">" + esc(label) + "</a>";
  }
  function teacherFileListHtml(files) {
    var html = "<ul class=\"pack-list\">";
    (files || []).forEach(function (f) {
      html += "<li>" + packDl(f.href, f.label) + "</li>";
    });
    html += "</ul>";
    return html;
  }
  function studentFileListHtml(files) {
    var html = "<ul class=\"pack-list\">";
    var n = 0;
    (files || []).forEach(function (f) {
      if (!studentHrefOk(f.href)) return;
      html += "<li>" + packDl(f.href, f.label) + "</li>";
      n += 1;
    });
    html += "</ul>";
    return n ? html : "<p>Material kommer</p>";
  }
  function teacherQuizListHtml(pack) {
    var html = "<ul class=\"pack-list\">";
    (pack.quizzes || []).forEach(function (q) {
      html += "<li><a href=\"#/" + q + "\">Quiz med facit</a></li>";
    });
    html += "</ul>";
    return html;
  }
  function teacherWeekPackHtml(cal) {
    var pack = weekPack(cal);
    var html = weekHeroHtml(cal);
    html += "<p class=\"lead\">" + esc(weekNames(cal)) + "</p>";
    if (!pack.ready) {
      html += "<article class=\"coming\"><h3>Pack kommer</h3><p>PDF och Word saknas. Bildspel och quiz finns.</p></article>";
      html += "<div class=\"pack-section\" data-pack=\"larare\"><ul class=\"pack-list\">";
      html += "<li>" + packDl(pack.pptx, "Bildspel, PowerPoint") + "</li>";
      html += "</ul>" + teacherQuizListHtml(pack) + "</div>";
      return html;
    }
    html += "<div class=\"pack-section\" data-pack=\"elev\">" + teacherFileListHtml(pack.elevFiles) + "</div>";
    html += "<div class=\"pack-section\" data-pack=\"larare\"><ul class=\"pack-list\">";
    html += "<li>" + packDl(pack.pptx, "Bildspel, PowerPoint") + "</li>";
    (pack.larareFiles || []).forEach(function (f) {
      html += "<li>" + packDl(f.href, f.label) + "</li>";
    });
    html += "</ul>" + teacherQuizListHtml(pack) + "</div>";
    return html;
  }
  function studentPostText(md) {
    var s = String(md || "");
    var parts = s.split(/\n---\s*\n/);
    if (parts.length > 1) s = parts.slice(1).join("\n---\n");
    return stripFacit(s);
  }
  function typeTabsHtml() {
    return "<p class=\"type-tabs\"><span class=\"post-type\">INLÄGG</span><span class=\"post-type\">MATERIAL</span><span class=\"post-type\">UPPGIFT</span><span class=\"post-type\">QUIZ</span></p>";
  }
  function isClassroomPost(path) {
    path = path || "";
    if (path.indexOf("-quiz.md") !== -1 || path.indexOf("-slides.md") !== -1) return false;
    return /classroom-v/.test(path);
  }
  function hashPath() {
    var raw = (location.hash || "").replace(/^#\/?/, "");
    try { return decodeURIComponent(raw).trim(); }
    catch (e) { return raw.trim(); }
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
  function stripFacit(md) {
    var s = String(md || "");
    var m = s.match(/^## Facit/im);
    if (!m) return s.trim();
    return s.slice(0, m.index).trim();
  }
  function scrubHtml(html) {
    if (isTeacher()) return String(html || "");
    var s = String(html || "");
    s = s.replace(/href=("|')[^"']*facit[^"']*("|')/gi, "href=\"#/\"");
    s = s.replace(/href=("|')[^"']*larare-[^"']*("|')/gi, "href=\"#/\"");
    s = s.replace(/href=("|')[^"']*\.pptx[^"']*("|')/gi, "href=\"#/\"");
    return s;
  }
  function mdHtml(md, path) {
    var src = rewriteMd(md, path || "");
    var html = (typeof marked !== "undefined" && marked.parse) ? marked.parse(src) : src;
    return scrubHtml(html);
  }
  function esc(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }
  function lozengeHtml(code) {
    var raw = String(code || "").toUpperCase().replace(/\s+/g, "");
    if (/^M\d$/.test(raw)) raw = "M0" + raw.charAt(1);
    if (/^\d+$/.test(raw)) raw = "M" + (raw.length < 2 ? "0" + raw : raw);
    return "<span class=\"lozenge mod-id " + raw.toLowerCase() + "\">" + esc(raw) + "</span>";
  }
  function stationHtml(code, extra) {
    var raw = String(code || "").toUpperCase().replace(/\s+/g, "");
    if (raw.charAt(0) !== "V") raw = "V" + raw;
    var cls = "station " + raw.toLowerCase();
    if (extra) cls += " " + extra;
    return "<span class=\"" + cls + "\">" + esc(raw) + "</span>";
  }
  function getProgress() {
    try { return JSON.parse(localStorage.getItem(PROGRESS_KEY) || "{}") || {}; }
    catch (e) { return {}; }
  }
  function markVisited(path) {
    if (!path || !isStudent()) return;
    var p = getProgress();
    p[path] = 1;
    localStorage.setItem(PROGRESS_KEY, JSON.stringify(p));
  }
  function isVisited(path) { return !!getProgress()[path]; }
  function classify(item) {
    var p = item && item.path ? item.path : "";
    if (p.indexOf("/lektioner/") !== -1) return "lektion";
    if (p.indexOf("bok/") === 0) return "bok";
    if (p.indexOf("-slides.md") !== -1) return "slides";
    if (p.indexOf("-quiz.md") !== -1) return "quiz";
    if (p.indexOf("classroom-") !== -1) return "classroom";
    return "other";
  }
  function orderedSteps(week) {
    var by = {};
    (week.items || []).forEach(function (it) { by[classify(it)] = it; });
    var order = isTeacher() ? ["classroom", "slides", "quiz", "lektion", "bok"] : STUDENT_STEPS;
    return order.map(function (k) { return by[k]; }).filter(Boolean);
  }
  function hubIndex(hub) {
    for (var i = 0; i < MODULES.length; i++) if (MODULES[i].hub === hub) return i;
    return -1;
  }
  function hubStationLabel(hub) {
    var idx = hubIndex(hub);
    if (idx < 0) return String(hub);
    return "V" + MODULES[idx].cal + " · " + MODULES[idx].m;
  }
  function calHubs(cal) {
    var out = [];
    for (var i = 0; i < MODULES.length; i++) if (MODULES[i].cal === String(cal)) out.push(MODULES[i].hub);
    return out;
  }
  function calModules(cal) {
    var out = [];
    for (var i = 0; i < MODULES.length; i++) if (MODULES[i].cal === String(cal)) out.push(MODULES[i]);
    return out;
  }
  function findItem(path) {
    var i, j, extra;
    for (i = 0; i < WEEKS.length; i++) {
      for (j = 0; j < WEEKS[i].items.length; j++) {
        if (WEEKS[i].items[j].path === path) return WEEKS[i].items[j];
      }
    }
    extra = extraList();
    for (i = 0; i < extra.length; i++) {
      if (extra[i].path === path) return extra[i];
    }
    return null;
  }
  function locatePath(path) {
    var i, j, steps;
    for (i = 0; i < WEEKS.length; i++) {
      steps = orderedSteps(WEEKS[i]);
      for (j = 0; j < steps.length; j++) {
        if (steps[j].path === path) {
          return { weekIdx: i, step: j + 1, total: steps.length, item: steps[j], mod: MODULES[i], steps: steps };
        }
      }
    }
    var extra = extraList();
    for (i = 0; i < extra.length; i++) {
      if (extra[i].path === path) return { extra: extra[i], item: extra[i] };
    }
    return { item: findItem(path) };
  }
  function chapterOf(path) {
    var i, it;
    for (i = 0; i < WEEKS.length; i++) {
      it = WEEKS[i].items.filter(function (x) { return x.path === path && x.figure; })[0];
      if (it) return { n: i + 1, title: MODULES[i].chap, path: it.path, figure: it.figure, caption: it.caption || "", cal: MODULES[i].cal, hub: MODULES[i].hub, weekIdx: i };
    }
    return null;
  }
  function allChapters() {
    var out = [];
    for (var i = 0; i < WEEKS.length; i++) {
      for (var j = 0; j < WEEKS[i].items.length; j++) {
        var it = WEEKS[i].items[j];
        if (it.figure && it.path.indexOf("bok/") === 0) {
          out.push({ n: out.length + 1, title: MODULES[i].chap, path: it.path, figure: it.figure, caption: it.caption || "", cal: MODULES[i].cal, hub: MODULES[i].hub, weekIdx: i });
        }
      }
    }
    return out;
  }
  function okPath(path) {
    if (!path || path.indexOf("..") !== -1) return false;
    if (hasFacit(path) && !isTeacher()) return false;
    if (isStudent() && isStudentForbidden(path)) return false;
    var lower = path.toLowerCase();
    var isMd = lower.slice(-3) === ".md";
    var isElevPack = /(^|\/)elev-[^/]+\.(pdf|docx)$/i.test(path);
    var isLektionPack = /(^|\/)lektion-[^/]+\.(pdf|docx)$/i.test(path);
    if (isBook()) {
      if (!isMd || path.indexOf("bok/") !== 0) return false;
      if (path === "bok/kapitellista-v2.md" || path === "bok/forord-vid-luckan.md") return true;
      return !!findItem(path) || !!chapterOf(path);
    }
    if (isStudent()) {
      if (isElevPack || isLektionPack) return true;
      if (!isMd) return false;
      if (path.indexOf("kurs/") !== 0) return false;
      if (path === "kurs/labbdag-v2.md") return true;
      if (path === "kurs/prov/skriftligt-prov-elev.md") return true;
      if (path === "kurs/kurskarta/kurskarta-v2.md") return true;
      if (isClassroomPost(path)) return false;
      if (path.indexOf("-slides.md") !== -1) return false;
      if (/^kurs\/elevblad\/.*-elev\.md$/i.test(path)) return true;
      var it = findItem(path);
      if (!it) return false;
      return classify(it) === "quiz";
    }
    if (isTeacher()) {
      if (!isMd) return false;
      if (path.indexOf("kurs/") !== 0 && path.indexOf("bok/") !== 0) return false;
      if (path === "bok/kapitellista-v2.md") return true;
      if (path === "bok/forord-vid-luckan.md") return true;
      if (path === "kurs/prov/skriftligt-prov-facit.md") return true;
      if (path === "kurs/labbdag-v2.md") return true;
      if (path.indexOf("kurs/elevblad/") === 0) return true;
      if (path.indexOf("kurs/lararhandledning/") === 0) return true;
      return !!findItem(path);
    }
    return false;
  }
  function parseQuiz(md) {
    var split = String(md || "").split(/^## Facit/im);
    var body = split[0] || "";
    var facit = split[1] || "";
    var answers = {};
    facit.split("\n").forEach(function (line) {
      var am = line.match(/^\s*(\d+)\.\s*([ABC])\b/i);
      if (am) answers[am[1]] = am[2].toUpperCase();
    });
    var questions = [];
    var re = /\*\*Fråga\s+(\d+)\.\*\*\s*/g;
    var idxs = [];
    var m;
    while ((m = re.exec(body))) {
      idxs.push({ n: m[1], start: m.index, end: m.index + m[0].length });
    }
    if (!idxs.length) return null;
    for (var i = 0; i < idxs.length; i++) {
      var chunkStart = idxs[i].end;
      var chunkEnd = i + 1 < idxs.length ? idxs[i + 1].start : body.length;
      var chunk = body.slice(chunkStart, chunkEnd);
      var lines = chunk.split("\n");
      var prompt = [];
      var options = [];
      var cur = null;
      var txt = "";
      for (var k = 0; k < lines.length; k++) {
        var om = lines[k].match(/^([ABC])\.\s*(.*)$/);
        if (om) {
          if (cur) options.push({ letter: cur, text: txt.trim() });
          cur = om[1];
          txt = om[2] || "";
        } else if (cur) {
          if (/^\s*---\s*$/.test(lines[k])) { /* skip */ }
          else if (lines[k].trim()) txt += " " + lines[k].trim();
        } else if (!/^\s*---\s*$/.test(lines[k])) {
          prompt.push(lines[k]);
        }
      }
      if (cur) options.push({ letter: cur, text: txt.trim() });
      var letters = options.map(function (o) { return o.letter; }).join("");
      if (options.length < 3 || letters.indexOf("A") < 0 || letters.indexOf("B") < 0 || letters.indexOf("C") < 0) return null;
      var num = idxs[i].n;
      if (!answers[num]) return null;
      questions.push({ n: num, prompt: prompt.join("\n").trim(), options: options, answer: answers[num] });
    }
    return { intro: body.slice(0, idxs[0].start).trim(), questions: questions, facitMd: facit.trim() };
  }
  function parseSlides(md) {
    var parts = String(md || "").split(/^## Slide\s+/im);
    if (parts.length < 2) return null;
    var slides = [];
    for (var i = 1; i < parts.length; i++) {
      var chunk = parts[i];
      var nl = chunk.indexOf("\n");
      var heading = (nl === -1 ? chunk : chunk.slice(0, nl)).trim();
      var rest = nl === -1 ? "" : chunk.slice(nl + 1);
      var nm = rest.split(/^Notes:\s*/im);
      var body = (nm[0] || "").replace(/^\s*---\s*$/gm, "").trim();
      var notes = nm.length > 1 ? nm.slice(1).join("Notes: ").replace(/^\s*---\s*$/gm, "").trim() : "";
      slides.push({ heading: heading, body: body, notes: notes });
    }
    return slides.length ? slides : null;
  }
  function parseGrades(md) {
    var found = { g: "", vg: "", ig: "" };
    var lines = String(md || "").split("\n");
    var cur = null, buf = [];
    function flush() {
      var t = buf.join(" ").replace(/\s+/g, " ").trim();
      if (cur && t) found[cur] = t;
    }
    for (var i = 0; i < lines.length; i++) {
      var gm = lines[i].match(/^\*\*(G|VG[^*]*|IG):\*\*\s*(.*)$/);
      if (gm) {
        flush();
        buf = [];
        var key = gm[1].toUpperCase().indexOf("VG") === 0 ? "vg" : gm[1].toLowerCase();
        cur = key;
        if (gm[2]) buf.push(gm[2]);
      } else if (cur) {
        if (/^## /.test(lines[i]) || /^\*\*[A-ZÅÄÖ]/.test(lines[i]) || /^\|/.test(lines[i])) {
          flush(); cur = null; buf = [];
        } else if (lines[i].trim()) buf.push(lines[i].trim());
      }
    }
    flush();
    if (!found.g && !found.vg && !found.ig) return null;
    return found;
  }
  function setBar(html) {
    var bar = byId("course-bar");
    if (!html) { bar.hidden = true; bar.innerHTML = ""; return; }
    bar.hidden = false;
    bar.innerHTML = html;
  }
  function navItems() {
    if (isTeacher()) {
      return [
        { href: "#/", nav: "pack", label: "Pack" },
        { href: "#/facit", nav: "facit", label: "Facit" }
      ];
    }
    if (isBook()) {
      return [
        { href: "#/", nav: "omslag", label: "Omslag" },
        { href: "#/innehall", nav: "innehall", label: "Innehåll" }
      ];
    }
    return [
      { href: "#/", nav: "strom", label: "Ström" },
      { href: "#/vecka", nav: "vecka", label: "Vecka" },
      { href: "#/labbdag", nav: "labbdag", label: "Labbdag" },
      { href: "#/prov", nav: "prov", label: "Prov" }
    ];
  }
  function paintNav(active) {
    var nav = byId("top-nav");
    if (!nav) return;
    var html = "";
    navItems().forEach(function (it) {
      html += "<a href=\"" + it.href + "\" data-nav=\"" + it.nav + "\"" + (it.nav === active ? " class=\"active\"" : "") + ">" + it.label + "</a>";
    });
    html += "<button type=\"button\" class=\"ghost\" id=\"lock-btn\">Lås</button>";
    nav.innerHTML = html;
    var lock = byId("lock-btn");
    if (lock) lock.addEventListener("click", lockNow);
  }
  function setNav(active) { paintNav(active); }
  function applyChrome() {
    var role = getRole();
    document.documentElement.setAttribute("data-role", role);
    if (role === "teacher") setShell("larare");
    else if (role === "book") setShell("bok");
    else setShell("elev");
    var k = byId("brand-kicker");
    if (k) {
      if (role === "teacher") k.innerHTML = "<span class=\"xfer\">LÄRARE</span> Pack";
      else if (role === "book") k.innerHTML = "<span class=\"xfer\">BOK</span> Fartyg och automation";
      else k.innerHTML = "<span class=\"xfer\">ELEV</span> Ström";
    }
    var home = byId("home-link");
    if (home) home.textContent = role === "book" ? "Vid luckan" : "Elteknik och ellära";
    document.title = role === "book" ? "Vid luckan" : "Elteknik och ellära";
  }
  function setShell(name) { document.documentElement.setAttribute("data-shell", name); }
  function setMain(html, wide) {
    var el = byId("main");
    el.className = wide ? "main wide" : "main";
    el.innerHTML = html;
    window.scrollTo(0, 0);
  }
  function weekVisited(cal) {
    var hubs = calHubs(cal);
    if (isVisited("vecka/" + cal)) return true;
    for (var i = 0; i < hubs.length; i++) {
      var idx = hubIndex(hubs[i]);
      if (idx < 0) continue;
      if (isVisited("vecka/" + hubs[i])) return true;
      var items = WEEKS[idx].items;
      for (var j = 0; j < items.length; j++) if (isVisited(items[j].path)) return true;
    }
    return false;
  }
  function miniLinks(idx) {
    var steps = orderedSteps(WEEKS[idx]);
    var names = { lektion: "lektion", bok: "kapitel", slides: "bildspel", quiz: "quiz" };
    var html = "<div class=\"mini-links\">";
    steps.forEach(function (st) {
      var k = classify(st);
      if (!names[k]) return;
      html += "<a href=\"#/" + st.path + "\">" + names[k] + "</a>";
    });
    html += "</div>";
    return html;
  }
  function weekNames(cal) {
    return calHubs(cal).map(function (h) { return MODULES[hubIndex(h)].name; }).join(" · ");
  }
  function studentWeekCard(cal) {
    var done = weekVisited(cal) ? " <span class=\"check\">✓</span>" : "";
    var mods = calModules(cal);
    var html = "<article class=\"card week-card\" data-v=\"" + cal + "\">";
    html += "<a class=\"week-title\" href=\"#/vecka/" + cal + "\">";
    html += stationHtml("V" + cal, "week-num");
    html += "<h3>Vecka " + cal + done + "</h3>";
    html += "<span class=\"lozenge-row\">";
    for (var i = 0; i < mods.length; i++) html += lozengeHtml(mods[i].m);
    if (mods.length > 1) html += "<span class=\"xfer\">byte</span>";
    html += "</span>";
    html += "<p class=\"path-line\">" + esc(weekNames(cal)) + "</p>";
    html += "<p class=\"path-line\">INLÄGG · MATERIAL · UPPGIFT · QUIZ</p>";
    html += "</a></article>";
    return html;
  }
  function teacherWeekCard(cal) {
    var mods = calModules(cal);
    var html = "<article class=\"card week-card\" data-v=\"" + cal + "\">";
    html += "<a class=\"week-title\" href=\"#/vecka/" + cal + "\">";
    html += stationHtml("V" + cal, "week-num");
    html += "<h3>Vecka " + cal + "</h3>";
    html += "<span class=\"lozenge-row\">";
    for (var i = 0; i < mods.length; i++) html += lozengeHtml(mods[i].m);
    if (mods.length > 1) html += "<span class=\"xfer\">byte</span>";
    html += "</span>";
    html += "<p class=\"path-line\">" + esc(weekNames(cal)) + "</p>";
    html += "<p class=\"path-line\">Pack · Bildspel · Quiz</p>";
    html += "</a></article>";
    return html;
  }
  function weekGridHtml() {
    var html = "<div class=\"week-grid\">";
    for (var i = 0; i < CAL_IDS.length; i++) {
      html += isTeacher() ? teacherWeekCard(CAL_IDS[i]) : studentWeekCard(CAL_IDS[i]);
    }
    html += "</div>";
    return html;
  }
  function latestReadyCal() {
    for (var i = CAL_IDS.length - 1; i >= 0; i--) {
      if (weekPack(CAL_IDS[i]).ready) return CAL_IDS[i];
    }
    return "1";
  }
  function showStudentHome() {
    setShell("elev");
    setNav("strom");
    setBar("");
    var latest = latestReadyCal();
    var head = "";
    head += "<p class=\"kicker\">Klassens ström</p>";
    head += "<h2>Elteknik och ellära</h2>";
    head += "<p class=\"lead\">Inlägg, material, uppgift och quiz. Inte en filträd.</p>";
    head += weekGridHtml();
    head += "<p class=\"kicker\" style=\"margin-top:2rem\">Senaste · V" + latest + "</p>";
    head += weekHeroHtml(latest);
    head += "<p class=\"lead\">" + esc(weekNames(latest)) + "</p>";
    showStudentStream(latest, { head: head, noTurn: true });
  }
  function showStudentCourse() {
    setShell("elev");
    setNav("vecka");
    setBar("");
    var html = "<p class=\"kicker\">Uppgifter</p><h2>Vecka</h2>";
    html += "<p class=\"lead\">Öppna veckan. Där ligger strömmen.</p>";
    html += weekGridHtml();
    setMain(html, true);
  }
  function stepCardHtml(item, n) {
    var k = classify(item);
    var html = "<a class=\"card step-card\" href=\"#/" + item.path + "\">";
    html += "<span class=\"step-n\">" + n + "</span>";
    if (item.figure) html += "<img class=\"thumb\" src=\"" + item.figure + "\" alt=\"" + esc(item.caption || item.label) + "\">";
    html += "<span class=\"step-body\"><span class=\"step-k\">" + esc(STEP_NAME[k] || "") + "</span><strong>" + esc(item.label) + "</strong></span>";
    if (isVisited(item.path)) html += "<span class=\"check\">✓</span>";
    html += "</a>";
    return html;
  }
  function teacherBetygCard(idx, n) {
    var info = MODULES[idx];
    var html = "<a class=\"card step-card\" href=\"#/vecka/" + info.hub + "/betyg\">";
    html += "<span class=\"step-n\">" + n + "</span>";
    html += "<span class=\"step-body\"><span class=\"step-k\">Säg så här</span><strong>G · VG · IG</strong></span>";
    html += "</a>";
    return html;
  }
  function modulePathHtml(idx) {
    var info = MODULES[idx];
    var steps = orderedSteps(WEEKS[idx]);
    var html = "<div class=\"mod-block\">";
    html += "<h3>" + lozengeHtml(info.m) + " " + esc(info.name) + "</h3>";
    html += "<ol class=\"path\">";
    for (var i = 0; i < steps.length; i++) html += "<li>" + stepCardHtml(steps[i], i + 1) + "</li>";
    if (isTeacher()) html += "<li>" + teacherBetygCard(idx, steps.length + 1) + "</li>";
    html += "</ol></div>";
    return html;
  }
  function turnHtml(prevHref, prevLabel, nextHref, nextLabel) {
    var html = "<nav class=\"week-turn\">";
    html += prevHref ? "<a href=\"" + prevHref + "\">Föregående station · " + esc(prevLabel) + "</a>" : "<span></span>";
    html += nextHref ? "<a href=\"" + nextHref + "\">Nästa station · " + esc(nextLabel) + "</a>" : "<span></span>";
    html += "</nav>";
    return html;
  }
  function calTurn(cal) {
    var i = CAL_IDS.indexOf(String(cal));
    var prevH = i > 0 ? "#/vecka/" + CAL_IDS[i - 1] : "#/";
    var prevL = i > 0 ? "V" + CAL_IDS[i - 1] : "Start";
    var nextH, nextL;
    if (i < CAL_IDS.length - 1) { nextH = "#/vecka/" + CAL_IDS[i + 1]; nextL = "V" + CAL_IDS[i + 1]; }
    else { nextH = isTeacher() ? "#/facit" : "#/prov"; nextL = isTeacher() ? "Facit" : "Prov"; }
    return turnHtml(prevH, prevL, nextH, nextL);
  }
  function hubTurn(hub) {
    var i = HUB_IDS.indexOf(String(hub));
    var prevH = i > 0 ? "#/vecka/" + HUB_IDS[i - 1] : "#/";
    var prevL = i > 0 ? hubStationLabel(HUB_IDS[i - 1]) : "Start";
    var nextH, nextL;
    if (i < HUB_IDS.length - 1) { nextH = "#/vecka/" + HUB_IDS[i + 1]; nextL = hubStationLabel(HUB_IDS[i + 1]); }
    else { nextH = isTeacher() ? "#/facit" : "#/prov"; nextL = isTeacher() ? "Facit" : "Prov"; }
    return turnHtml(prevH, prevL, nextH, nextL);
  }
  function showStudentStream(cal, opts) {
    opts = opts || {};
    var pack = weekPack(cal);
    var html = opts.head || ("<p class=\"kicker\">Ström</p>" + weekHeroHtml(cal) + "<p class=\"lead\">" + esc(weekNames(cal)) + "</p>");
    if (!opts.head) {
      if (cal === "9") html += "<p class=\"mini-links\"><a href=\"#/prov\">Skriftligt prov</a></p>";
      if (cal === "8") html += "<p class=\"mini-links\"><a href=\"#/labbdag\">Labbdag efter vecka 8</a></p>";
    }
    html += typeTabsHtml();
    if (!pack.ready) {
      html += "<article class=\"stream-post\" data-type=\"material\">" + stationHtml("V" + cal, "week-num") + "<h3>Material kommer</h3></article>";
      if (!opts.noTurn) html += calTurn(cal);
      setMain(html, true);
      return;
    }
    html += "<div id=\"stream-root\"></div>";
    if (!opts.noTurn) html += calTurn(cal);
    setMain(html, true);
    var inlaggP = pack.inlagg
      ? fetch(pack.inlagg).then(function (r) { return r.ok ? r.text() : ""; }).catch(function () { return ""; })
      : Promise.resolve("");
    var quizPath = pack.quizzes && pack.quizzes[0] ? pack.quizzes[0] : "";
    var quizP = quizPath
      ? fetch(quizPath).then(function (r) { return r.ok ? r.text() : ""; }).catch(function () { return ""; })
      : Promise.resolve("");
    Promise.all([inlaggP, quizP]).then(function (parts) {
      var root = byId("stream-root");
      if (!root) return;
      var out = "";
      var inlaggMd = studentPostText(parts[0] || "");
      out += "<article class=\"stream-post\" data-type=\"inlagg\">";
      out += inlaggMd ? mdHtml(inlaggMd, pack.inlagg) : "<p>Inget inlägg.</p>";
      out += "</article>";
      out += "<article class=\"stream-post\" data-type=\"material\">";
      out += studentFileListHtml(pack.materialFiles && pack.materialFiles.length ? pack.materialFiles : pack.elevFiles);
      out += "</article>";
      out += "<article class=\"stream-post\" data-type=\"uppgift\">";
      out += studentFileListHtml(pack.uppgiftFiles);
      if (pack.elevMd) out += "<p><a href=\"#/" + pack.elevMd + "\">Läs på skärmen</a></p>";
      out += "</article>";
      var quizMd = parts[1] || "";
      var quiz = parseQuiz(quizMd);
      out += "<article class=\"stream-post\" data-type=\"quiz\">";
      if (quiz) out += renderQuiz(quiz, quizPath);
      else if (quizPath) out += "<p><a href=\"#/" + quizPath + "\">Öppna quiz</a></p>";
      else out += "<p>Material kommer</p>";
      out += "</article>";
      root.innerHTML = out;
      if (quiz) bindQuiz();
    });
  }
  function showWeek(id) {
    var cal = String(id).replace(/b$/, "");
    if (CAL_IDS.indexOf(cal) === -1) { showBlocked(); return; }
    markVisited("vecka/" + id);
    if (isTeacher()) {
      setShell("larare");
      setNav("pack");
      setBar("");
      var th = "<p class=\"kicker\">Pack</p>";
      th += teacherWeekPackHtml(cal);
      th += calTurn(cal);
      setMain(th, true);
      return;
    }
    setShell("elev");
    setNav("vecka");
    setBar("");
    showStudentStream(cal);
  }
  function showTeacherHome() {
    setShell("larare");
    setNav("pack");
    setBar("");
    var html = "";
    html += "<p class=\"kicker\">Lärare</p>";
    html += "<h2>Pack</h2>";
    html += "<p class=\"lead\">Ladda ner till Classroom. Klistra inlägget. Facit och lärarfiler går inte till elever.</p>";
    html += "<div class=\"cta-row\">";
    html += "<a class=\"cta\" href=\"#/vecka/1\">" + stationHtml("V1", "week-num") + "<span><strong>Pack V1</strong><span>Elsäkerhet och stötar</span></span></a>";
    html += "<a class=\"cta\" href=\"#/facit\"><strong>Facit</strong><span>Prov och quiz</span></a>";
    html += "</div>";
    html += weekGridHtml();
    html += "<p class=\"foot-note\">Labbdag efter vecka 8. Skriftligt prov i vecka 9. Facit bara här.</p>";
    setMain(html, true);
  }
  function showKorschema() {
    setShell("larare");
    setNav("korschema");
    setBar("");
    var html = "<p class=\"kicker\">Kalender</p><h2>Körschema</h2>";
    html += "<p class=\"lead\">Tolv moduler på nio kalenderveckor. Distans i Classroom. En fysisk dag efter vecka 8.</p>";
    html += "<table class=\"cal-table\"><thead><tr><th>Vecka</th><th>Moduler</th><th>Gör så här</th></tr></thead><tbody>";
    var tips = {
      "1": "Klistra inlägget. 16 slides. Quiz skall vs upplysning.",
      "2": "Isolering. Inte 1 MΩ som lag.",
      "3": "Resistiv DC. Mätning och räkning.",
      "4": "Enfas AC.",
      "5": "Trefas och spänningstyper ombord.",
      "6": "Maskiner.",
      "7": "Två moduler: eltavla och verktyg.",
      "8": "Ritningar och hållkrets. Därefter labbdag.",
      "9": "Elarbete/IP och felsökning. Skriftligt prov."
    };
    for (var i = 0; i < CAL_IDS.length; i++) {
      var cal = CAL_IDS[i];
      html += "<tr><td><a href=\"#/vecka/" + cal + "\">" + stationHtml("V" + cal, "week-num") + " Vecka " + cal + "</a></td><td>";
      var mods = calModules(cal);
      for (var mi = 0; mi < mods.length; mi++) html += lozengeHtml(mods[mi].m) + " ";
      if (mods.length > 1) html += "<span class=\"xfer\">byte</span> ";
      html += esc(weekNames(cal)) + "</td><td>" + esc(tips[cal] || "") + "</td></tr>";
    }
    html += "</tbody></table>";
    html += "<article class=\"card ticket\" style=\"margin-top:1.2rem\"><p class=\"kicker\">En fysisk dag</p><h3>Labbdag efter vecka 8</h3><p class=\"path-line\">Varv. Titta, inte live-wire. En dag.</p><p class=\"mini-links\"><a href=\"#/labbdag\">Öppna labbdagen</a></p></article>";
    setMain(html, true);
  }
  function showFacitHub() {
    setShell("larare");
    if (!isTeacher()) { showBlocked(); return; }
    setNav("facit");
    setBar("");
    var html = "<p class=\"kicker\">Lärare</p><h2>Facit</h2>";
    html += "<p class=\"lead\">Skriftligt prov och quizfacit. Inte i Classroom mot elever.</p>";
    html += "<div class=\"prov-grid\">";
    html += "<a class=\"card\" href=\"#/kurs/prov/skriftligt-prov-facit.md\"><span class=\"step-k\">Prov</span><h3>Skriftligt prov, facit</h3></a>";
    html += "<a class=\"card\" href=\"#/kurs/prov/skriftligt-prov-elev.md\"><span class=\"step-k\">Elevblad</span><h3>Skriftligt prov, elev</h3></a>";
    html += "<a class=\"card\" href=\"#/kurs/lararhandledning/classroom-v-prov-vecka9.md\"><span class=\"step-k\">Classroom</span><h3>Provvecka, inlägg</h3></a>";
    html += "</div>";
    html += "<h3 style=\"margin-top:2rem\">Quizfacit per vecka</h3><div class=\"prov-grid\">";
    for (var i = 0; i < WEEKS.length; i++) {
      var q = WEEKS[i].items.filter(function (it) { return classify(it) === "quiz"; })[0];
      if (!q) continue;
      html += "<a class=\"card\" href=\"#/" + q.path + "\"><span class=\"step-k\">" + esc(WEEKS[i].title) + "</span><h3>" + esc(q.label) + "</h3></a>";
    }
    html += "</div>";
    setMain(html, true);
  }
  function showBetyg(hub) {
    setShell("larare");
    if (!isTeacher()) { showBlocked(); return; }
    var idx = hubIndex(hub);
    if (idx < 0) { showBlocked(); return; }
    var info = MODULES[idx];
    var by = {};
    WEEKS[idx].items.forEach(function (it) { by[classify(it)] = it; });
    setNav("pack");
    setBar("<div class=\"bar-inner\"><span>" + stationHtml("V" + info.cal) + " " + lozengeHtml(info.m) + " G–VG–IG</span></div>");
    function paint(grades, facitNote) {
      var html = "<p class=\"kicker\">Säg så här</p><h2>" + esc(info.name) + "</h2>";
      html += "<p class=\"lead\">Läs upp målen. Klistra inte lagtext. 1 MΩ är inte skall.</p>";
      html += "<div class=\"grades\">";
      html += "<article class=\"card\"><h3>G</h3><p>" + esc((grades && grades.g) || "Målen i lektionen sitter. Säkerhetssvaren är rätt.") + "</p></article>";
      html += "<article class=\"card\"><h3>VG</h3><p>" + esc((grades && grades.vg) || "G med egen motiverad bedömning.") + "</p></article>";
      html += "<article class=\"card ig\"><h3>IG</h3><p>" + esc((grades && grades.ig) || "Säkerhetsfälla. JFB-jakt. 1 MΩ som lag.") + "</p></article>";
      html += "</div>";
      if (facitNote) html += "<aside class=\"facit-panel\"><h3>Quizspår</h3>" + mdHtml(facitNote, by.quiz ? by.quiz.path : "") + "</aside>";
      html += "<p class=\"mini-links\"><a href=\"#/vecka/" + info.hub + "\">Tillbaka till veckan</a></p>";
      setMain(html);
    }
    var waits = [];
    if (by.lektion) waits.push(fetch(by.lektion.path).then(function (r) { return r.ok ? r.text() : ""; }));
    else waits.push(Promise.resolve(""));
    if (by.quiz) waits.push(fetch(by.quiz.path).then(function (r) { return r.ok ? r.text() : ""; }));
    else waits.push(Promise.resolve(""));
    Promise.all(waits).then(function (parts) {
      paint(parseGrades(parts[0] || ""), parts[1] ? stripFacitToTail(parts[1]) : "");
    }).catch(function () { paint(null, ""); });
  }
  function stripFacitToTail(md) {
    var s = String(md || "");
    var m = s.match(/^## Facit/im);
    if (!m) return "";
    return s.slice(m.index).trim();
  }
  function showBookHome(asCover) {
    setShell("bok");
    setNav(isBook() ? (asCover ? "omslag" : "innehall") : "bok");
    setBar("");
    if (isBook() && asCover) {
      var cover = "<section class=\"cover\"><p class=\"kicker\">Vid luckan</p><h2>Vid luckan</h2><p class=\"sub\">Elteori för elingenjörer och elektriker ombord.</p></section>";
      cover += "<div id=\"luckan\" class=\"luckan\"></div>";
      cover += "<p class=\"toc-extra\"><a href=\"#/innehall\">Till innehållet</a></p>";
      setMain(cover);
      fetch("bok/forord-vid-luckan.md").then(function (r) { return r.ok ? r.text() : ""; }).then(function (md) {
        var el = byId("luckan");
        if (!el) return;
        var body = String(md || "");
        var cut = body.lastIndexOf("\n---\n");
        if (cut !== -1) body = body.slice(0, cut);
        el.innerHTML = mdHtml(body, "bok/forord-vid-luckan.md");
      }).catch(function () {
        var el = byId("luckan");
        if (el) el.innerHTML = "<p class=\"page-err\">Kunde inte läsa sidan.</p>";
      });
      return;
    }
    var ch = allChapters();
    var html = "<p class=\"kicker\">Innehåll</p><h2>Tolv kapitel</h2>";
    html += "<p class=\"lead\">M01–M12. En figur per kapitel.</p>";
    html += "<ol class=\"chapter-list\">";
    for (var i = 0; i < ch.length; i++) {
      var c = ch[i];
      var done = isVisited(c.path) ? " <span class=\"check\">✓</span>" : "";
      html += "<li><a class=\"card chapter-row\" href=\"#/" + c.path + "\">";
      html += lozengeHtml(MODULES[c.weekIdx].m);
      html += "<span class=\"n\">" + c.n + "</span>";
      html += "<img class=\"thumb\" src=\"" + c.figure + "\" alt=\"" + esc(c.caption) + "\">";
      html += "<span class=\"step-body\"><span class=\"step-k\">" + esc(MODULES[c.weekIdx].m) + "</span><h3>" + esc(c.title) + done + "</h3></span>";
      html += "</a></li>";
    }
    html += "</ol>";
    setMain(html, true);
  }
  function showProv() {
    setShell("elev");
    if (isBook()) { showBlocked(); return; }
    if (isTeacher()) { showFacitHub(); return; }
    setNav("prov");
    setBar("");
    var html = "<p class=\"kicker\">" + stationHtml("V9") + " Prov</p><h2>Prov</h2>";
    html += "<p class=\"lead\">Skriftligt prov. Bara elevbladet. Facit ligger inte här.</p>";
    html += "<div class=\"prov-grid\">";
    html += "<a class=\"card\" href=\"#/kurs/prov/skriftligt-prov-elev.md\"><span class=\"step-k\">Prov</span><h3>Skriftligt prov</h3></a>";
    html += "</div>";
    setMain(html, true);
  }
  function showBlocked() {
    setBar("");
    var msg = "Den sidan finns inte.";
    if (isStudent()) msg = "Den sidan finns inte för elever. Facit är låst.";
    if (isBook()) msg = "Bara boken i den här inloggningen.";
    setMain("<p class=\"page-err\">" + msg + "</p>");
  }
  function courseBarFor(path) {
    var loc = locatePath(path);
    if (loc.mod) {
      var nextHref;
      if (loc.step < loc.total) nextHref = "#/" + loc.steps[loc.step].path;
      else if (isTeacher()) nextHref = "#/vecka/" + loc.mod.hub + "/betyg";
      else if (loc.weekIdx + 1 < WEEKS.length) nextHref = "#/vecka/" + MODULES[loc.weekIdx + 1].hub;
      else nextHref = "#/prov";
      var left = "<a href=\"#/vecka/" + loc.mod.hub + "\">" + stationHtml("V" + loc.mod.cal) + "</a> " + lozengeHtml(loc.mod.m) + " " + esc(loc.mod.name) + " · Steg " + loc.step + "/" + loc.total;
      return "<div class=\"bar-inner\"><span>" + left + "</span><a href=\"" + nextHref + "\">Nästa station</a></div>";
    }
    if (/labbdag/i.test(path)) return "<div class=\"bar-inner\"><span>Labbdag</span></div>";
    if (/prov/i.test(path) || hasFacit(path)) return "<div class=\"bar-inner\"><span><a href=\"" + (isTeacher() ? "#/facit" : "#/prov") + "\">Prov</a></span></div>";
    if (path.indexOf("bok/") === 0) {
      var chapBar = chapterOf(path);
      if (chapBar) {
        var bmod = MODULES[chapBar.weekIdx];
        return "<div class=\"bar-inner\"><span>" + lozengeHtml(bmod.m) + " " + esc(bmod.chap) + "</span><a href=\"" + (isBook() ? "#/innehall" : "#/") + "\">Innehåll</a></div>";
      }
      return "<div class=\"bar-inner\"><span><a href=\"" + (isBook() ? "#/innehall" : "#/") + "\">Innehåll</a></span></div>";
    }
    return "";
  }
  function renderQuiz(parsed, path) {
    var html = "<div class=\"quiz\" id=\"quiz-root\">";
    if (parsed.intro) html += "<div class=\"quiz-intro\">" + mdHtml(parsed.intro, path) + "</div>";
    parsed.questions.forEach(function (q) {
      html += "<div class=\"q\" data-n=\"" + q.n + "\" data-answer=\"" + q.answer + "\">";
      html += "<p class=\"q-n\">Fråga " + q.n + "</p>";
      html += "<div class=\"q-prompt\">" + mdHtml(q.prompt, path) + "</div><div class=\"q-opts\">";
      q.options.forEach(function (o) {
        html += "<button type=\"button\" data-letter=\"" + o.letter + "\">" + o.letter + ". " + esc(o.text) + "</button>";
      });
      html += "</div><p class=\"q-fb\" hidden></p></div>";
    });
    html += "<p class=\"quiz-score\" hidden></p></div>";
    if (isTeacher() && parsed.facitMd) {
      html += "<aside class=\"facit-panel\" id=\"facit-panel\"><h3>Facit</h3>" + mdHtml("## Facit\n" + parsed.facitMd, path) + "</aside>";
    }
    return html;
  }
  function bindQuiz() {
    var root = byId("quiz-root");
    if (!root) return;
    var qs = root.querySelectorAll(".q");
    var answered = 0, correct = 0, total = qs.length;
    var score = root.querySelector(".quiz-score");
    qs.forEach(function (qel) {
      var ans = qel.getAttribute("data-answer");
      qel.querySelectorAll("[data-letter]").forEach(function (btn) {
        btn.addEventListener("click", function () {
          if (qel.getAttribute("data-done")) return;
          qel.setAttribute("data-done", "1");
          var pick = btn.getAttribute("data-letter");
          var ok = pick === ans;
          answered += 1;
          if (ok) correct += 1;
          qel.querySelectorAll("[data-letter]").forEach(function (b) {
            b.disabled = true;
            if (b.getAttribute("data-letter") === ans) b.classList.add("correct");
            if (b === btn && !ok) b.classList.add("wrong");
          });
          var fb = qel.querySelector(".q-fb");
          fb.hidden = false;
          fb.textContent = ok ? "Rätt" : "Fel";
          fb.className = "q-fb " + (ok ? "ok" : "no");
          if (answered === total) {
            score.hidden = false;
            score.textContent = "Resultat: " + correct + " av " + total + " rätt.";
          }
        });
      });
    });
  }
  function bindSlides(slides, path) {
    var root = byId("deck-root");
    if (!root) return;
    var i = 0;
    function draw() {
      var s = slides[i];
      var html = "<p class=\"deck-meta\">Bild " + (i + 1) + " av " + slides.length + "</p>";
      html += "<div class=\"slide\"><h2>Slide " + esc(s.heading) + "</h2>";
      html += "<div class=\"slide-body\">" + mdHtml(s.body, path) + "</div></div>";
      if (s.notes && isTeacher()) html += "<div class=\"notes\"><strong>Talk track</strong>" + mdHtml(s.notes, path) + "</div>";
      html += "<div class=\"deck-nav\">";
      html += "<button type=\"button\" class=\"ghost\" id=\"deck-prev\"" + (i === 0 ? " disabled" : "") + ">Föregående</button>";
      html += "<button type=\"button\" id=\"deck-next\"" + (i === slides.length - 1 ? " disabled" : "") + ">Nästa</button>";
      html += "</div>";
      root.innerHTML = html;
      var prev = byId("deck-prev");
      var next = byId("deck-next");
      if (prev) prev.addEventListener("click", function () { if (i > 0) { i -= 1; draw(); } });
      if (next) next.addEventListener("click", function () { if (i < slides.length - 1) { i += 1; draw(); } });
    }
    draw();
  }
  function chapterFooter(path) {
    var chs = allChapters();
    var idx = -1, i;
    for (i = 0; i < chs.length; i++) if (chs[i].path === path) idx = i;
    if (idx < 0) return "";
    var html = "<nav class=\"chap-nav\">";
    html += idx > 0 ? "<a href=\"#/" + chs[idx - 1].path + "\">Föregående kapitel · " + chs[idx - 1].n + "</a>" : "<span></span>";
    html += idx < chs.length - 1 ? "<a href=\"#/" + chs[idx + 1].path + "\">Nästa kapitel · " + chs[idx + 1].n + "</a>" : "<span></span>";
    html += "</nav>";
    html += "<p class=\"toc-extra\"><a href=\"#/innehall\">Innehåll</a></p>";
    return html;
  }
  function showDoc(path) {
    if (!okPath(path)) { showBlocked(); return; }
    if (path.indexOf("bok/") === 0) setShell("bok");
    else if (isTeacher() && (path.indexOf("lararhandledning") !== -1 || path.indexOf("-slides.md") !== -1)) setShell("larare");
    else setShell(isTeacher() ? "larare" : "elev");
    if (isBook()) setNav("innehall");
    else if (path.indexOf("bok/") === 0) setNav(isTeacher() ? "pack" : "kursen");
    else if (path.indexOf("labbdag") !== -1) setNav(isTeacher() ? "pack" : "labbdag");
    else if (hasFacit(path)) setNav("facit");
    else if (path.indexOf("prov") !== -1) setNav(isTeacher() ? "facit" : "prov");
    else setNav(isTeacher() ? "pack" : "vecka");
    setBar(courseBarFor(path));
    fetch(path).then(function (res) {
      if (!res.ok) throw new Error(String(res.status));
      return res.text();
    }).then(function (md) {
      markVisited(path);
      var html = "";
      var item = findItem(path);
      var chap = chapterOf(path);
      var fig = chap || (item && item.figure ? item : null);
      if (chap) {
        var cmod = MODULES[chap.weekIdx];
        html += "<p class=\"kicker chap-mark\">" + lozengeHtml(cmod.m) + (isBook() ? "" : (" " + stationHtml("V" + chap.cal))) + " " + esc(cmod.chap) + "</p>";
      }
      if (fig && fig.figure) {
        html += "<figure class=\"figure\"><img src=\"" + fig.figure + "\" alt=\"" + esc(fig.caption || "") + "\">";
        if (fig.caption) html += "<figcaption>" + esc(fig.caption) + "</figcaption>";
        html += "</figure>";
      }
      var after = null;
      if (path.indexOf("-quiz.md") !== -1) {
        var quiz = parseQuiz(md);
        if (quiz) { html += renderQuiz(quiz, path); after = bindQuiz; }
        else html += mdHtml(isTeacher() ? md : stripFacit(md), path);
      } else if (path.indexOf("-slides.md") !== -1) {
        var slides = parseSlides(md);
        if (slides) {
          html += "<div class=\"deck\" id=\"deck-root\"></div>";
          after = function () { bindSlides(slides, path); };
        } else html += mdHtml(md, path);
      } else {
        html += mdHtml(isTeacher() ? md : stripFacit(md), path);
      }
      if (chap) html += chapterFooter(path);
      setMain(html);
      if (after) after();
    }).catch(function () {
      setMain("<p class=\"page-err\">Kunde inte läsa sidan.</p>");
    });
  }
  function showLab() {
    setShell("elev");
    if (isBook()) { showBlocked(); return; }
    setNav("labbdag");
    setBar("<div class=\"bar-inner\"><span>Labbdag · efter V8</span></div>");
    fetch("kurs/labbdag-v2.md").then(function (res) {
      if (!res.ok) throw new Error(String(res.status));
      return res.text();
    }).then(function (md) {
      markVisited("kurs/labbdag-v2.md");
      var html = "<article class=\"card ticket\" style=\"margin-bottom:1.4rem\"><p class=\"kicker\">Biljett</p><h3>En fysisk dag</h3><p class=\"path-line\">Efter vecka 8. Varv. Titta, inte live-wire.</p></article>";
      html += mdHtml(md, "kurs/labbdag-v2.md");
      setMain(html);
    }).catch(function () {
      setMain("<p class=\"page-err\">Kunde inte läsa sidan.</p>");
    });
  }
  function route() {
    applyChrome();
    var raw = hashPath();
    if (hasFacit(raw) && !isTeacher()) { showBlocked(); return; }
    if (isStudent() && isStudentForbidden(raw)) { showBlocked(); return; }
    if (isBook()) {
      if (!raw) { showBookHome(true); return; }
      if (raw === "innehall" || raw === "bok") { showBookHome(false); return; }
      if (okPath(raw) && raw.indexOf("bok/") === 0) { showDoc(raw); return; }
      showBlocked(); return;
    }
    if (isTeacher()) {
      if (!raw || raw === "pack") { showTeacherHome(); return; }
      if (raw === "korschema") { showKorschema(); return; }
      if (raw === "facit") { showFacitHub(); return; }
      if (raw === "labbdag") { showLab(); return; }
      if (raw === "bok" || raw === "innehall") { showBookHome(false); return; }
      var tb = raw.match(/^vecka\/(\d+b?)\/betyg$/);
      if (tb) { showBetyg(tb[1]); return; }
      var tw = raw.match(/^vecka\/(\d+b?)$/);
      if (tw) { showWeek(tw[1]); return; }
      if (okPath(raw)) { showDoc(raw); return; }
      showBlocked(); return;
    }
    if (!raw) { showStudentHome(); return; }
    if (raw === "kursen" || raw === "vecka") { showStudentCourse(); return; }
    if (raw === "bok" || raw === "innehall") { showBlocked(); return; }
    if (raw === "labbdag") { showLab(); return; }
    if (raw === "prov") { showProv(); return; }
    var sw = raw.match(/^vecka\/(\d+b?)$/);
    if (sw) { showWeek(sw[1]); return; }
    if (okPath(raw) && /\.(pdf|docx|pptx)$/i.test(raw)) { showBlocked(); return; }
    if (okPath(raw)) { showDoc(raw); return; }
    showBlocked();
  }
  function showApp() {
    applyChrome();
    byId("gate").hidden = true;
    byId("app").hidden = false;
    paintNav("");
    route();
  }
  function showGate() {
    byId("gate").hidden = false;
    byId("app").hidden = true;
    document.documentElement.removeAttribute("data-role");
    document.documentElement.setAttribute("data-shell", "elev");
  }
  function lockNow() {
    clearSession();
    var pw = byId("pw");
    if (pw) pw.value = "";
    showGate();
  }
  function onHash() {
    if (!isOpen()) { showGate(); return; }
    route();
  }
  function initGate() {
    var form = byId("gate-form");
    var err = byId("gate-err");
    var picker = byId("role-picker");
    var chosen = "";
    picker.addEventListener("click", function (e) {
      var btn = e.target.closest ? e.target.closest(".role-btn") : null;
      if (!btn) return;
      chosen = btn.getAttribute("data-role") || "";
      var btns = picker.querySelectorAll(".role-btn");
      for (var i = 0; i < btns.length; i++) {
        btns[i].setAttribute("aria-pressed", btns[i] === btn ? "true" : "false");
      }
      err.hidden = true;
    });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var role = chosen;
      var spec = ROLES[role];
      if (!spec) { err.hidden = false; return; }
      var pw = byId("pw").value.trim();
      sha256hex(pw).then(function (h) {
        if (h === spec.hash) {
          err.hidden = true;
          setSession(role);
          showApp();
        } else {
          err.hidden = false;
        }
      });
    });
    byId("main").addEventListener("click", function (e) {
      var a = e.target.closest ? e.target.closest("a") : null;
      if (!a) return;
      var href = a.getAttribute("href") || "";
      var decoded = href;
      try { decoded = decodeURIComponent(href); } catch (err2) {}
      if (!isTeacher() && (hasFacit(href) || hasFacit(decoded))) {
        e.preventDefault();
        showBlocked();
        return;
      }
      if (isStudent() && (isStudentForbidden(href) || isStudentForbidden(decoded))) {
        e.preventDefault();
        showBlocked();
      }
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
