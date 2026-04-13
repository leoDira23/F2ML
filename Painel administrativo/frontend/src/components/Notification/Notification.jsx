import "./Notification.css";

export default function Notification({ texto, onClose }) {
  if (!texto) return null;

  return (
    <>
      <div className="overlay" onClick={onClose}></div>
      <div className="toast">
        {texto}
      </div>
    </>
  );
}