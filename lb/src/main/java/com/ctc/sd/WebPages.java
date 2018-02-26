package com.ctc.sd;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.context.embedded.EmbeddedWebApplicationContext;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class WebPages {
    @Autowired
    EmbeddedWebApplicationContext server;

    @RequestMapping("/user/test")
    @ResponseBody
    public String home() {
        return "Hello World!"
                + " / "
                + server.getEmbeddedServletContainer().getPort();
    }
}
