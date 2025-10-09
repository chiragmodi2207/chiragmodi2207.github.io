import { createContext, useContext, useMemo, useReducer, useState, createElement, useEffect } from "react"
import { applyDelta, ReflexEvent, hydrateClientStorage, useEventLoop, refs } from "$/utils/state"
import { jsx } from "@emotion/react";

export const initialState = {"reflex___state____state": {"is_hydrated_rx_state_": false, "router_rx_state_": {"session": {"client_token": "", "client_ip": "", "session_id": ""}, "headers": {"host": "", "origin": "", "upgrade": "", "connection": "", "cookie": "", "pragma": "", "cache_control": "", "user_agent": "", "sec_websocket_version": "", "sec_websocket_key": "", "sec_websocket_extensions": "", "accept_encoding": "", "accept_language": "", "raw_headers": {}}, "page": {"host": "", "path": "", "raw_path": "", "full_path": "", "full_raw_path": "", "params": {}}, "url": "", "route_id": ""}}, "reflex___state____state.app___states___state____state": {"is_submitting_rx_state_": false, "services_rx_state_": [{"icon": "landmark", "title": "UK Accounting", "description": "Comprehensive accounting services for UK-based businesses, ensuring compliance and efficiency. Our team helps you navigate the complexities of UK tax laws, from day-to-day bookkeeping to annual statutory filings.", "items": [{"name": "Bookkeeping", "description": "Meticulous record-keeping to ensure your financial data is accurate and up-to-date."}, {"name": "VAT Return", "description": "Timely and accurate VAT return submissions to keep you compliant with HMRC regulations."}, {"name": "Self Assessment", "description": "Hassle-free self-assessment tax return services for individuals and sole traders."}, {"name": "Annual Account", "description": "Preparation and submission of annual accounts for limited companies, ensuring statutory compliance."}]}, {"icon": "globe", "title": "Indian Accounting", "description": "Expert financial services tailored to the Indian market, covering all statutory requirements. We provide end-to-end solutions for individuals and businesses, ensuring accurate tax filing and compliance with the latest regulations.", "items": [{"name": "Income Tax Return", "description": "Filing of income tax returns for individuals, HUFs, and businesses as per Indian tax laws."}, {"name": "GST Return", "description": "Complete GST compliance, from registration to monthly and annual return filings."}, {"name": "Accounting", "description": "Full-service accounting solutions for Indian businesses to maintain clean and compliant books."}, {"name": "Audit", "description": "Statutory and internal audit services to ensure financial accuracy and regulatory adherence."}]}], "team_rx_state_": [{"name": "Eleanor Vance", "role": "Managing Partner, CPA", "avatar_url": "https://api.dicebear.com/9.x/initials/svg?seed=EleanorVance"}, {"name": "Marcus Thorne", "role": "Senior Tax Consultant", "avatar_url": "https://api.dicebear.com/9.x/initials/svg?seed=MarcusThorne"}, {"name": "Isabelle Reed", "role": "Lead Auditor", "avatar_url": "https://api.dicebear.com/9.x/initials/svg?seed=IsabelleReed"}, {"name": "Julian Knox", "role": "Business Advisor", "avatar_url": "https://api.dicebear.com/9.x/initials/svg?seed=JulianKnox"}], "testimonials_rx_state_": [{"name": "John Doe", "role": "CEO, Tech Innovators", "quote": "Their expertise in financial consulting was pivotal for our company's growth. Truly a game-changer.", "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=John"}, {"name": "Jane Smith", "role": "Founder, Creative Co.", "quote": "The most professional and responsive accounting team I've ever worked with. They make tax season stress-free.", "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Jane"}, {"name": "Samuel Green", "role": "Director, BuildRight", "quote": "Audit and assurance services were delivered with exceptional detail and clarity. Highly recommended.", "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=Samuel"}]}, "reflex___state____state.reflex___state____frontend_event_exception_state": {}, "reflex___state____state.reflex___state____on_load_internal_state": {}, "reflex___state____state.reflex___state____update_vars_internal_state": {}}

export const defaultColorMode = "light"
export const ColorModeContext = createContext(null);
export const UploadFilesContext = createContext(null);
export const DispatchContext = createContext(null);
export const StateContexts = {reflex___state____state: createContext(null),reflex___state____state__app___states___state____state: createContext(null),reflex___state____state__reflex___state____frontend_event_exception_state: createContext(null),reflex___state____state__reflex___state____on_load_internal_state: createContext(null),reflex___state____state__reflex___state____update_vars_internal_state: createContext(null),};
export const EventLoopContext = createContext(null);
export const clientStorage = {"cookies": {}, "local_storage": {}, "session_storage": {}}


export const state_name = "reflex___state____state"

export const exception_state_name = "reflex___state____state.reflex___state____frontend_event_exception_state"

// These events are triggered on initial load and each page navigation.
export const onLoadInternalEvent = () => {
    const internal_events = [];

    // Get tracked cookie and local storage vars to send to the backend.
    const client_storage_vars = hydrateClientStorage(clientStorage);
    // But only send the vars if any are actually set in the browser.
    if (client_storage_vars && Object.keys(client_storage_vars).length !== 0) {
        internal_events.push(
            ReflexEvent(
                'reflex___state____state.reflex___state____update_vars_internal_state.update_vars_internal',
                {vars: client_storage_vars},
            ),
        );
    }

    // `on_load_internal` triggers the correct on_load event(s) for the current page.
    // If the page does not define any on_load event, this will just set `is_hydrated = true`.
    internal_events.push(ReflexEvent('reflex___state____state.reflex___state____on_load_internal_state.on_load_internal'));

    return internal_events;
}

// The following events are sent when the websocket connects or reconnects.
export const initialEvents = () => [
    ReflexEvent('reflex___state____state.hydrate'),
    ...onLoadInternalEvent()
]
    

export const isDevMode = false;

export function UploadFilesProvider({ children }) {
  const [filesById, setFilesById] = useState({})
  refs["__clear_selected_files"] = (id) => setFilesById(filesById => {
    const newFilesById = {...filesById}
    delete newFilesById[id]
    return newFilesById
  })
  return createElement(
    UploadFilesContext.Provider,
    { value: [filesById, setFilesById] },
    children
  );
}

export function ClientSide(component) {
  return ({ children, ...props }) => {
    const [Component, setComponent] = useState(null);
    useEffect(() => {
      setComponent(component);
    }, []);
    return Component ? jsx(Component, props, children) : null;
  };
}

export function EventLoopProvider({ children }) {
  const dispatch = useContext(DispatchContext)
  const [addEvents, connectErrors] = useEventLoop(
    dispatch,
    initialEvents,
    clientStorage,
  )
  return createElement(
    EventLoopContext.Provider,
    { value: [addEvents, connectErrors] },
    children
  );
}

export function StateProvider({ children }) {
  const [reflex___state____state, dispatch_reflex___state____state] = useReducer(applyDelta, initialState["reflex___state____state"])
const [reflex___state____state__app___states___state____state, dispatch_reflex___state____state__app___states___state____state] = useReducer(applyDelta, initialState["reflex___state____state.app___states___state____state"])
const [reflex___state____state__reflex___state____frontend_event_exception_state, dispatch_reflex___state____state__reflex___state____frontend_event_exception_state] = useReducer(applyDelta, initialState["reflex___state____state.reflex___state____frontend_event_exception_state"])
const [reflex___state____state__reflex___state____on_load_internal_state, dispatch_reflex___state____state__reflex___state____on_load_internal_state] = useReducer(applyDelta, initialState["reflex___state____state.reflex___state____on_load_internal_state"])
const [reflex___state____state__reflex___state____update_vars_internal_state, dispatch_reflex___state____state__reflex___state____update_vars_internal_state] = useReducer(applyDelta, initialState["reflex___state____state.reflex___state____update_vars_internal_state"])
  const dispatchers = useMemo(() => {
    return {
      "reflex___state____state": dispatch_reflex___state____state,
"reflex___state____state.app___states___state____state": dispatch_reflex___state____state__app___states___state____state,
"reflex___state____state.reflex___state____frontend_event_exception_state": dispatch_reflex___state____state__reflex___state____frontend_event_exception_state,
"reflex___state____state.reflex___state____on_load_internal_state": dispatch_reflex___state____state__reflex___state____on_load_internal_state,
"reflex___state____state.reflex___state____update_vars_internal_state": dispatch_reflex___state____state__reflex___state____update_vars_internal_state,
    }
  }, [])

  return (
    createElement(StateContexts.reflex___state____state,{value: reflex___state____state},
createElement(StateContexts.reflex___state____state__app___states___state____state,{value: reflex___state____state__app___states___state____state},
createElement(StateContexts.reflex___state____state__reflex___state____frontend_event_exception_state,{value: reflex___state____state__reflex___state____frontend_event_exception_state},
createElement(StateContexts.reflex___state____state__reflex___state____on_load_internal_state,{value: reflex___state____state__reflex___state____on_load_internal_state},
createElement(StateContexts.reflex___state____state__reflex___state____update_vars_internal_state,{value: reflex___state____state__reflex___state____update_vars_internal_state},
    createElement(DispatchContext, {value: dispatchers}, children)
    )))))
  )
}