function timeConversion(s) {
  let [hh, mm, ssUnit] = s.split(":");
  const unit = ssUnit.includes("PM") ? "PM" : "AM";
  const [ss, _] = ssUnit.split(unit);
  if (unit === "AM" && +hh === 12) hh = "00";
  else if (unit === "PM" && +hh !== 12) {
    hh = (+hh + 12) % 24;
  }
  return `${hh}:${mm}:${ss}`;
}
