document.addEventListener('DOMContentLoaded', function() {
  const currentDate = new Date();
  const calendar = document.getElementById('calendar');

  function renderCalendar(year, month) {
    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);
    const startingDay = firstDay.getDay();
    const daysInMonth = lastDay.getDate();

    const monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

    calendar.innerHTML = '';

    // Header
    const header = document.createElement('tr');
    header.innerHTML = `
      <th colspan="7">${monthNames[month]} ${year}</th>
    `;
    calendar.appendChild(header);

    // Days of the week
    const daysOfWeek = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    const daysOfWeekRow = document.createElement('tr');
    daysOfWeek.forEach(day => {
      const th = document.createElement('th');
      th.textContent = day;
      daysOfWeekRow.appendChild(th);
    });
    calendar.appendChild(daysOfWeekRow);

    // Days
    let date = 1;
    for (let i = 0; i < 6; i++) {
      const weekRow = document.createElement('tr');
      for (let j = 0; j < 7; j++) {
        if (i === 0 && j < startingDay) {
          const td = document.createElement('td');
          weekRow.appendChild(td);
        } else if (date > daysInMonth) {
          break;
        } else {
          const td = document.createElement('td');
          td.textContent = date;
          if (year === currentDate.getFullYear() && month === currentDate.getMonth() && date === currentDate.getDate()) {
            td.classList.add('today');
          }
          weekRow.appendChild(td);
          date++;
        }
      }
      calendar.appendChild(weekRow);
    }
  }

  renderCalendar(currentDate.getFullYear(), currentDate.getMonth());

  document.addEventListener('click', function(event) {
    if (event.target.tagName === 'TD') {
      const selectedDate = parseInt(event.target.textContent);
      if (!isNaN(selectedDate)) {
        alert(`You clicked on ${selectedDate}/${currentDate.getMonth() + 1}/${currentDate.getFullYear()}`);
      }
    }
  });
});